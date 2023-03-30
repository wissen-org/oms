import json

def getMenuList():
    with open('data.json') as user_file:
        file_contents = user_file.read()
    obj = json.loads(file_contents)
    return obj['menu']

with open('settings.json') as user_file:
    file_contents = user_file.read()
obj = json.loads(file_contents)

def getPhone():
    return str(obj['phone'])

def getFontStrings(font_name):
    if(font_name==""):
        return list(obj['font']["default"].values()) 
    return list(obj['font'][font_name].values())


def getPrintMode():
    return bool(obj['print-mode'])