import os, json

def mach_json(in_file, out_path):
    os.makedirs(os.path.join(out_path, "check"), exist_ok=True)
    os.makedirs(os.path.join(out_path, "normal"), exist_ok=True)
    total_dict = dict()
    label_data = []
    try:
        with open(INTERNAL_IMG_PATH+'/'+in_file, 'r') as img_json:
            img_dict = json.load(img_json)
            label = img_dict['image_inside_info']['annotations']
            for i in label:
                label_data.append(i['image_label'])
            img_dict['data_info']['multi_modal_label'] = label_data
            total_dict = img_dict
        file_name, old_extension = os.path.splitext(os.path.basename(in_file))
        with open(INTERNAL_WAV_PATH+'/'+file_name[:-2]+"AI.json", 'r') as ai_json:
            ai_dict = json.load(ai_json)
            total_dict['audio_inside_info'] = ai_dict
        with open(EXTERNAL_WAV_PATH+'/'+file_name[:-2]+"AO.json", 'r') as ao_json:
            ao_dict = json.load(ao_json)
            total_dict['audio_outside_info'] = ao_dict
    except:
        return 
    ao_label = total_dict['audio_outside_info']['audio_outside_label']
    ai_label = total_dict['audio_inside_info']['audio_inside_label']
    
    if ("A" in [ao_label, ai_label] and "A1" in label_data):
        multi_label_path = os.path.join(out_path, "check")
        # total_dict['audio_inside_info']['audio_inside_label'] = "N"
        # total_dict['audio_outside_info']['audio_outside_label'] = "N"
    elif  ("N" in [ao_label, ai_label] and "A5" in label_data):
        multi_label_path = os.path.join(out_path, "check")
        # total_dict['audio_inside_info']['audio_inside_label'] = "A"
        # total_dict['audio_outside_info']['audio_outside_label'] = "A"
    else:
        multi_label_path = os.path.join(out_path, "normal")
    multi_label_total_path = os.path.join(multi_label_path, in_file)
    with open(multi_label_total_path, 'w', encoding='utf-8') as f:
        json.dump(total_dict, f, indent = 4, ensure_ascii=False)

def json_main(img_path, ai_path, ao_path, out_path):
    file_list = [f for f in os.listdir(img_path) if f.endswith(".json")]
    global INTERNAL_IMG_PATH
    INTERNAL_IMG_PATH = img_path
    global INTERNAL_WAV_PATH 
    INTERNAL_WAV_PATH = ai_path
    global EXTERNAL_WAV_PATH
    EXTERNAL_WAV_PATH = ao_path
    for file in file_list:
        mach_json(file, out_path)
        
    
