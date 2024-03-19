import json
import os
import bot_loging as log

def check_for_file(file_path):
    if os.path.isfile(file_path):
        return True
    else:
        return False
    

def check_json_empty(file_path):
    if check_for_file(file_path): # file exists
        with open(file_path, 'r') as file:
            file_content = file.read()
            if len(file_content) == 0: # file empty
                return True
            else: # file not empty
                
                write_json(log.get_json_init(), file_path)
                return False
    else: # file does not exist
        create_log_file(file_path)
        return True

def create_log_file(file_path):
    with open(file_path, 'w') as file:
        json.dump({}, file)

def write_json(data, file_path):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)