import librosa
import soundfile as sf
import os, wave, json
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
import numpy as np
from scipy.io import wavfile
import pandas as pd
import cv2
import copy

'''
    특정 폴더를 입력받아 해당 폴더의 wav 폴더안의 wav파일을 찾아 해당 파일을
    특정 시간단위로 잘라내어 wav 폴더에 저장하며, json 폴더에 json 데이터를 저장한다.
    입력값 :
        1. 잘라낼 오디오 파일
        2. 해당 파일의 분류번호 (1-9)
        3. 내부, 외부 음향 (AI, AO)
        4. 음향을 자를 시작 시간 (초) | 지정하지 않을 경우 0초로 지정
        5. 저장할 폴더 경로  |  지정하지 않을 경우 output_dir 폴더로 지정
        6. 자를 시간 단위 (초)  | 지정하지 않을 경우 5초로 설정
'''

TIME_UNIT = 2
TYPE_JSON = 'json'
TYPE_WAV = 'wav'
SEGMENT_S = 100

DURATION = 5

AI_NOISE_START = 39

# AI_TARGET_1_START = 8
# AI_TARGET_1_END = 12
# AI_TARGET_2_START = 29
# AI_TARGET_2_END = 38

AI_TARGET_1_START = 6
AI_TARGET_1_END = 21
AI_TARGET_2_START = 57
AI_TARGET_2_END = 63

AO_TARGET_START = 10
AO_TARGET_END = 24

AI_PADING_SIZE = 1.7
AO_PADING_SIZE = 1.5

ex_info = {
    "audio_outside_id": "",
    "audio_outside_file_name": "",
    "audio_outside_original_file_name": "",
    "audio_outside_num_channels": "",
    "audio_outside_sample_width": "",
    "audio_outside_frame_rate": "",
    "audio_outside_num_frames": "",
    "audio_outside_length": 5.0,
    "audio_outside_timestamp_start": "",
    "audio_outside_timestamp_end": "",
    "audio_outside_label": "N"
}

in_info = {
    "audio_inside_id": "",
    "audio_inside_file_name": "",
    "audio_inside_num_channels": "",
    "audio_inside_sample_width": "",
    "audio_inside_frame_rate": "",
    "audio_inside_num_frames": "",
    "audio_inside_length": 5.0,
    "audio_inside_timestamp_start": "",
    "audio_inside_timestamp_end": "",
    "audio_inside_label": "N"
}

gov_dict = {
    '제주시' : "JEJU",
    '시흥시' : 'SIHEUNG',
    '전주시' : 'JEONJU',
    '진도군' : 'JINDO'
}

pipe_type_dict = {
    '도수관' : 'A',
    '송수관' : 'B',
    '배수관' : 'C',
}

pipe_jindo_dict = {
    '도수관' : 'CA',
    '송수관' : 'CB',
    '배수관' : 'CC',
}

def change_path(in_file, out_folder, extension):

    file_name, old_extension = os.path.splitext(os.path.basename(in_file))
    new_file_name = file_name + extension
    new_file_path = os.path.join(out_folder, new_file_name)
    return new_file_path

def get_wav_param(in_file):
    
    with wave.open(in_file, 'rb') as wav_file:
        num_channels, sample_width, frame_rate, num_frames, _, _ = wav_file.getparams()
    # WAV 파일의 길이 계산 (초)
    duration_seconds = num_frames / frame_rate
    wav_info = {
        'file_path': in_file,
        'num_channels': num_channels,
        'sample_width': sample_width,
        'frame_rate': frame_rate,
        'num_frames': num_frames,
        'length(s)': round(duration_seconds,3)
    }

    return wav_info

def save_json(path, index, wavefile, start, end, type, time, num, gov, pipetype, label='N'):
    ai_info = get_wav_param(wavefile)
    _start_time = time+timedelta(seconds=start)
    _end_time = time+timedelta(seconds=end)
    _start = f'{_start_time.strftime("%Y%m%d %H:%M:%S")}'
    _end = f'{_end_time.strftime("%Y%m%d %H:%M:%S")}'
    if "AI" == type:
        side = "inside"
        info = in_info
        
    else :
        side = "outside"
        info = ex_info
        info[f'audio_{side}_original_file_name'] = f"{gov}_{pipetype}_{(index)}.{TYPE_WAV}"

    
    info[f'audio_{side}_id'] = f'{gov}_{pipetype}_{(index)}_{str(num)}'
    info[f'audio_{side}_file_name'] = f'{gov}_{pipetype}_{(index)}_{str(num)}_{type}.{TYPE_WAV}'
    info[f'audio_{side}_num_channels'] = ai_info['num_channels']
    info[f'audio_{side}_sample_width'] = ai_info['sample_width']
    info[f'audio_{side}_frame_rate'] = ai_info['frame_rate']
    info[f'audio_{side}_length'] = ai_info['length(s)']
    info[f'audio_{side}_num_frames'] = ai_info['num_frames']
    info[f'audio_{side}_timestamp_start'] = _start
    info[f'audio_{side}_timestamp_end'] = _end
    info[f'audio_{side}_label'] = label
    # json 파일로 저장

    json_file = f'{path}/{info[f"audio_{side}_id"]}_{type}.{TYPE_JSON}'
    with open(json_file, 'w', encoding='utf-8') as f:
        json.dump(info, f, indent = 4, ensure_ascii=False)
def save_label(path, file, type, label='N'):
    if "AI" == type:
        side = "inside"
    else :
        side = "outside"
    json_file = change_path(file, path, '.json')
    
    with open(json_file, 'r', encoding='utf-8') as file:
        data = json.load(file)

        data[f'audio_{side}_label'] = label
        with open(json_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent = 4, ensure_ascii=False)

def save_mel(y, sr, in_file, out_folder, type, save=True):
    n_fft = 1024
    S = librosa.feature.melspectrogram(y=y, sr=sr, n_fft=n_fft, hop_length=512, n_mels=96, fmax=5120) 
    mel_spect = librosa.power_to_db(S, ref=np.max)
    mel = np.sort(mel_spect, axis=1)
    fig, ax = plt.subplots()
    img = librosa.display.specshow(mel, y_axis='mel', sr=sr, ax=ax, fmax=5120)
    fig.colorbar(img, ax=ax, format="%+2.0f dB")
    plt.tight_layout(pad=0)
    out_file = change_path(in_file, out_folder, '.png')
    if save:
        plt.savefig(out_file, bbox_inches='tight', pad_inches=0, format='png')
    plt.close()   

    if 'AI' == type:
        for i, _mel in enumerate(mel):
            index = int(_mel.size*0.5) 
            mel[i][index:] = mel_spect.min() # 우측 50% 제거
        if mel[AI_TARGET_2_START:AI_TARGET_2_END].mean() > mel.mean()+AI_PADING_SIZE:
            if mel[AI_TARGET_2_END:].mean() >= mel[AI_TARGET_2_START:AI_TARGET_2_END].mean():
                return "N"
            return "A"
        return "N" 
    else:
        for i, _mel in enumerate(mel):
            index = int(_mel.size*0.2) 
            mel[i][index:] = mel_spect.min() # 우측 80% 제거
        if mel[AI_TARGET_1_START:AI_TARGET_1_END].mean() > mel.mean()+AO_PADING_SIZE:
            return "A"
        else:
            return 'N'
        
        
def save_stft(y, sr, in_file, out_folder):
    fig, ax = plt.subplots()
    D = librosa.amplitude_to_db(np.abs(librosa.stft(y)), ref=np.max)  
    img = librosa.display.specshow(D, sr=sr, x_axis='time', y_axis='log', fmax=5120)
    plt.tight_layout(pad=0)     
    os.makedirs(out_folder, exist_ok=True)
    out_file = change_path(in_file, out_folder, '.png')
    fig.colorbar(img, ax=ax, format="%+2.0f dB") 
    plt.savefig(out_file, bbox_inches='tight', pad_inches=0, format='png')    
    plt.close()


def split_main(file, dir, audiotype, gov, pipe, is_json, is_mel, is_stft, is_wav, vedio_time, csvfile):
    set_duration = DURATION
    half_duration = set_duration / 2
    if "AO" == audiotype:
        half_duration = set_duration
    start_time = 0
    end_time = half_duration
    current = 0.0
    end_duration = librosa.get_duration(path=file)
    file_segment = 0
    counter = 1
    print(end_duration)
    csv_list = pd.read_csv(csvfile)
    file_list = csv_list.values.tolist()
    wav_dir = os.path.join(dir, 'wav')
    mel_dir = os.path.join(dir, 'mel')
    stft_dir = os.path.join(dir, 'stft')
    json_dir = os.path.join(dir, 'json')
    y, sr = librosa.load(file, sr=None, duration=end_duration)
    y = librosa.util.normalize(y)
    for info in file_list:
        _, _, index, _, _ = info[4].split("_")
        index = (str(index).zfill(2))
        csv_index = int(info[0])

        

        file_index = int(f"{csv_index}0")
        file_index = (str(file_index).zfill(6))
        
        if "AI" == audiotype:
            hour, min, sec = map(float, info[1].split(":"))
            file_segment = hour * 3600 + min * 60 + sec
        else :
            file_segment += 5

        if current < half_duration:
            set_duration = end_time - start_time
        elif current + half_duration > end_duration:  
            #set_duration =  end_duration - start_time
            end_time = end_duration
            start_time = end_time - 5
        else:
            set_duration = DURATION

        pipe_type = pipe_type_dict[pipe]
        filename = f"{gov_dict[gov]}_{pipe_type}_{index}_{file_index}_{audiotype}.{TYPE_WAV}"
        output_file = os.path.join(wav_dir, filename)
        time = datetime.strptime(vedio_time, "%Y-%m-%d %H:%M:%S")
        
        #y = librosa.mu_compress(y, quantize=False)
        if start_time <= 0:
            start = 0
            end = 5
        else:
            start = start_time
            end = end_time
        s_y = int(start)*sr
        e_y = int(end)*sr
        ny = y[s_y:e_y]

        if is_wav:
            os.makedirs(wav_dir, exist_ok=True)
            sf.write(output_file, ny, sr)  
        if is_stft:
            save_stft(ny, sr, output_file, stft_dir)
        if is_mel:
            os.makedirs(mel_dir, exist_ok=True)
        label = save_mel(y=ny, sr=sr, out_folder=mel_dir, in_file=filename, type=audiotype, save=is_mel)
        if is_json:
            os.makedirs(json_dir, exist_ok=True)
            save_json(path=json_dir, index=index, wavefile=output_file, start=start_time, end=end_time, type=audiotype, label=label, time=time, gov=gov_dict[gov], pipetype=pipe_type, num=file_index)

        current = file_segment
        
        if "AI" == audiotype:
            start_time = current - half_duration
            end_time = current + half_duration
        else :
            print(start_time, end_time)
            start_time += 5 
            end_time += 5
            
        counter += 1

    return counter


# elif "AI" == audiotype and (current - half_duration) < 0 :
        #     end_time = set_duration