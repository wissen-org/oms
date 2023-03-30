import tokenGen as tg
import send
import module
import sys
import settings
import display
def sendProccess(rawMessage,phone=-1): #-1 phone means that phone no. is not available and 0 means that the user might have set the phone number and we want the system to pick the phone number form there
    if(phone==-1):
        if(rawMessage==""):
            _phone,_rawMessage = tg.captureSendTokens(False,False)
        else:
            _phone = tg.captureSendTokens(False,True)[0]
            _rawMessage = rawMessage
        send.sendWaMsg(_phone,_rawMessage)
    elif(phone==0):
        _phone = settings.getPhone()
        if(rawMessage==""):
            _rawMessage = tg.captureSendTokens(True,False)[1]
        else:
            _rawMessage = rawMessage
        send.sendWaMsg(_phone,_rawMessage)
    else:
        send.sendWaMsg(phone,rawMessage)

def generateMeetingUpdate():
    tokens = tg.captureGMUTokens()
    raw = module.generateMeetingUpdate(tokens)
    display.ptr(raw)
    sendProccess(raw,-1)

def generateTicket():
    tokens = tg.captureTixToken()
    raw = module.generateTicket(tokens)
    display.ptr(raw)
    sendProccess(raw,0)

def generateBoldPoints():
    pass


def quit():
    sys.exit()