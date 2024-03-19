import json
import datetime
import bot_util as util
import bot_paths as bp

blank_startUp:dict = {
    "id": int,
    "startUpTime": str
}

json_init:dict = {
    "startUp": [],
    "shutDown": [],
    "crash": []
}

def logStartUp():
    if util.check_for_file(bp.getLogPath()): #file exists
        if util.check_json_empty(bp.getLogPath()): #json empty
            util.write_json(json_init, bp.getLogPath())
        else: #json not empty
            data = getLog(bp.getLogPath())
            if len(data["startUp"]) > 0: #strartUp-log has at least one list entry
                data["startUp"].append(init_new_startUp(blank_startUp, get_last_id(data["startUp"])))
            else:
                data["startUp"].append(init_new_startUp(blank_startUp, -1))
            util.write_json(data, bp.getLogPath())
    else: #file does not exist
        util.write_json(json_init, bp.getLogPath())
        data = getLog(bp.getLogPath())
        data["startUp"].append(init_new_startUp(blank_startUp, -1))
        util.write_json(data, bp.getLogPath())

def init_new_startUp(data:dict, lastID:int) -> dict:
    data["id"] = lastID + 1
    data["startUpTime"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return data

def get_last_id(data:dict) -> int:
    return data[-1]["id"]

def getLog(file_path:str) -> dict:
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

def get_json_init() -> dict:
    return json_init