import os
import librosa
import cv2
import numpy as np


def change_path(in_file, out_folder, extension):

    file_name, old_extension = os.path.splitext(os.path.basename(in_file))
    new_file_name = file_name + extension
    new_file_path = os.path.join(out_folder, new_file_name)
    return new_file_path


def check_label(y, sr, out_folder):
    os.makedirs(out_folder, exist_ok=True)
    y = librosa.util.normalize(y)
    y = librosa.mu_compress(y, quantize=False)
    
    n_fft =1024
    S = librosa.feature.melspectrogram(y=y, sr=sr, n_fft=n_fft, hop_length=512, n_mels=128, fmin=1024, fmax=3072)
    mel_spect = librosa.power_to_db(S, ref=np.max)
    
    spectrogram = mel_spect.astype(np.uint8)
    bgr_image = cv2.applyColorMap(spectrogram, cv2.COLORMAP_VIRIDIS)
    gray = cv2.medianBlur(bgr_image, 5)
    gray = cv2.cvtColor(gray, cv2.COLOR_BGR2GRAY)
    _, dst5 = cv2.threshold(gray, gray.mean(), 255, cv2.THRESH_BINARY ) 
    horizontal_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 10))
    detected_lines = cv2.morphologyEx(dst5, cv2.MORPH_OPEN, horizontal_kernel, iterations=2)
    contours, hierarchy = cv2.findContours(detected_lines, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    label = "N"
    if len(contours):
        label = "A"
    return label    