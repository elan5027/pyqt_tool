import os, json
import openpyxl
def write_xl(WAV_DIR, FILE_NAME):
    file_dict = dict()
    wav_list = [f for f in os.listdir(WAV_DIR) if f.endswith(".json")]
    
    for file in wav_list:
        gov, type, num, name, end = file.split('_')
        direct = os.path.join(WAV_DIR, file)
        with open(direct, 'rb') as wf:
            json_data = json.load(wf)
            if 'AI' == end[:2]:
                file_dict[num+name] = json_data['audio_inside_label']
            else:
                file_dict[num+name] = json_data['audio_outside_label']
        
    workbook = openpyxl.Workbook()
    sheet = workbook.active
    j = 2
    sheet['A1'] = "index"
    sheet['B1'] = 'audio_label'

    for key, value in file_dict.items():
        sheet[f'A{j}'] = key
        sheet[f'B{j}'] = str(value)
        j += 1
    sheet["F1"] = "Count"
    sheet["G1"] = "Audio N"
    sheet["H1"] = "Audio A"
    sheet['F2'] = f'=COUNTA(B2:B{j})'
    sheet["G2"] = f'=COUNTIF(B2:B{j}, "N")'
    sheet["H2"] = f'=COUNTIF(B2:B{j}, "A")' 
    
    workbook.save(FILE_NAME+'.xlsx')
    workbook.close()
