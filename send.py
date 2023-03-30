import webbrowser

def sendWaMsg(phone,rawMessage):
    url = f"https://wa.me/{phone}?text={generateMsgString(rawMessage)}"
    openBrowser(url)

def generateMsgString(rawMessage):
    msg = rawMessage
    msg = msg.replace(" ","%20")
    msg = msg.replace("\n","%0A")
    return msg

def openBrowser(url):
    webbrowser.open(url)