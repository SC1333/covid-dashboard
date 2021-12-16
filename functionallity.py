import json

def time_convert(hhmm="00:00"):
    hh = ' '
    mm = ' '
    seconds = 1
    if hhmm is not None:
        hh = int(hhmm.split(':')[0])
        mm = int(hhmm.split(':')[1])
        mm = mm+(hh*60)
        seconds = mm*60
        return seconds
    return seconds


def get_config_data():
    config = open("config.json","r")
    config_data = json.load(config)
    return config_data




