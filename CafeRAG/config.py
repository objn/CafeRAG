import json

def read_file_config(file_path="config.json"):
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

def read_config(param, data):
    return data[param]

config_data = read_file_config()
print(read_config('Install_state', config_data))