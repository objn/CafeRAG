import os
import json

def add_code_to_file_after_line(main_file_path, src_code_or_path, search_line):
    # ตรวจสอบว่าพารามิเตอร์เป็นพาธของไฟล์หรือไม่
    if os.path.isfile(src_code_or_path):
        with open(src_code_or_path, 'r') as src_file:
            new_code = src_file.read()
    else:
        new_code = src_code_or_path

    with open(main_file_path, 'r') as main_file:
        lines = main_file.readlines()

    for i, line in enumerate(lines):
        if search_line in line:
            lines.insert(i + 1, new_code)
            break

    with open(main_file_path, 'w') as main_file:
        main_file.writelines(lines)

def add_code_to_file_before_line(main_file_path, src_code_or_path, search_line):
    if os.path.isfile(src_code_or_path):
        with open(src_code_or_path, 'r') as src_file:
            new_code = src_file.read()
    else:
        new_code = src_code_or_path

    with open(main_file_path, 'r') as main_file:
        lines = main_file.readlines()

    for i, line in enumerate(lines):
        if search_line in line:
            lines.insert(i - 1, new_code)
            break

    with open(main_file_path, 'w') as main_file:
        main_file.writelines(lines)

def read_file_config(file_path=os.getcwd() + "/CafeRAG/config.json"):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        print("The file was not found.")
        return None
    except json.JSONDecodeError:
        print("Error decoding JSON.")
        return None

def edit_config(param, valueofparam, file_path=os.getcwd() + "/CafeRAG/config.json"):
    try:
        # อ่านข้อมูลจากไฟล์ JSON
        with open(file_path, 'r') as file:
            data = json.load(file)
        
        # แก้ไขค่า Install_state
        data[param] = valueofparam
        
        # บันทึกข้อมูลกลับไปยังไฟล์ JSON
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)
        
        print("Install_state has been updated to True.")
        return data
    except FileNotFoundError:
        print("The file was not found.")
        return None
    except json.JSONDecodeError:
        print("Error decoding JSON.")
        return None

def read_config(param, data):
    return data[param]

def read_config_Patch_file(param, data):
    return read_config(param, read_config('Patch_files', read_config('Install_path', data)))
