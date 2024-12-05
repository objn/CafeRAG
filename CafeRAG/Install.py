from Installlib import logo
import os
import config

# SOURCE CODE

def setup_env():
    path = '/app/backend/data/CafeRAG/'
    sub_folder = ['knowledge_files','cache']
    # Ensure the main directory exists
    if not os.path.exists(path):
        os.makedirs(path)
        # Create each subfolder under the main directory
        for folder in sub_folder:
            folder_path = os.path.join(path, folder)
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)
                print(f"Created folder: {folder_path}")
            else:
                print(f"Folder already exists: {folder_path}")

        
# SOURCE CODE END

config_data = config.read_file_config()

if config.read_config('Install_state', config_data) == False:

    print(logo.installer())
    setup_env()
    # เรียกใช้เมธอดโดยระบุเส้นทางของไฟล์ที่เกี่ยวข้อง
    main_file = ['open-webui','fusion-data-import','fusion-data']
    src_file = ['']  # ไฟล์ที่มีโค้ดใหม่
    search_line = ['log.setLevel(SRC_LOG_LEVELS["MAIN"])','import requests', 'payload = json.dumps(payload)']

    for i in range(len(main_file)):
        if main_file[i-1] == 'open-webui':
            pathofile = os.getcwd() + config.read_config_Patch_file('Openwebui_main', config_data)
            config.add_code_to_file_after_line(pathofile, os.getcwd() + "/CafeRAG/Installlib/logo.txt", search_line[i-1])

        elif main_file[i-1] == 'fusion-data-import':
            pathofile = os.getcwd() + config.read_config_Patch_file('OpenAI_API_file', config_data)
            config.add_code_to_file_after_line(pathofile, os.getcwd() + "/CafeRAG/Installlib/import_CafeRAG.txt", search_line[i-1])

        elif main_file[i-1] == 'fusion-data':
            pathofile = os.getcwd() + config.read_config_Patch_file('OpenAI_API_file', config_data)
            config.add_code_to_file_before_line(pathofile, os.getcwd() + "/CafeRAG/Installlib/OpenAI_API.txt", search_line[i-1])

    config.edit_config('Install_state', True)