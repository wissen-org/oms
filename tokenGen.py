from datetime import datetime
import utilities as util
import display as dp

##CONSTANTS
font1 = "courier-sans"

def captureGMUTokens():
    desc = ask("description","text")
    tone = ask("tone","text")
    tag = ask("tag","text")
    audience = ask("target audience","text")
    guest = ask("residee","text")
    date = ask("date","date-time")
    time = ask("time","date-time")
    venue = ask("venue","text")
    agenda = ask("agenda","text")
    return [desc,tone,tag,audience,guest,date,time,venue,agenda]

def captureGTTokens():
    desc = ask("description","text")
    return [desc]


def captureTixToken():
    desc = ask("description","req-text")
    tagee = ask("name","name")
    return [desc]

def captureSendTokens(isPhoneAvail,isMsgAvail):
    phoneNum = -1
    msgString = ""
    if(not isPhoneAvail):
        phoneNum = ask("phone number","phone")
    if(not isMsgAvail):
        msgString = ask("message String","text")
    return [phoneNum,msgString]

def ask(followUpQuestion,type):
    usrInp = input(f"\n🤔 ＜{util.changeFont(followUpQuestion,font1)}＞\n({util.changeFont(type,font1)}) ")
    constraintCheckReport = checkConstraint(usrInp,type)
    if(constraintCheckReport == 'OK'):
        return usrInp
    else:
        dp.ptr(constraintCheckReport)
        return ask(followUpQuestion,type)
        
def checkConstraint(str,type):
    if(type=='num'):
        if(str.isnumeric()):
            return 'OK'
        else:
            return "❌ "+util.changeFont("Input NOT numeric, try again!",font1)
    elif(type=="phone"):
        if(util.validate_mobile_number(str)):
            return 'OK'
        else:
            return "❌ "+util.changeFont("Input NOT a phone number, try again!",font1)
    elif(type=="email"):
        if(util.validate_email_address(str)):
            return 'OK'
        else:
            return "❌ "+util.changeFont("Input NOT an email address, try again!",font1)
    elif(type=="req-text"):
        if(len(str)==0):
            return "❌ "+util.changeFont("Input text can NOT be empty, try again! USING \\0",font1)
        else:
            return 'OK'
    else:
        return "OK"
