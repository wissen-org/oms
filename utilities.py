from datetime import datetime, timedelta
import utilities
import re
import settings
# CONSTANTS
wissenName = "Student Organization, Wissen"
wissenNameTag = "Student Organization, Wissen under the aegis of youth affairs, Student Welfare Wing, Lovely Professional University - Phagwara, Punjab."
wissenMembers = "Wissenites"

# tone : humble > Firsts Imression, Clients or Members
# pronoun :  

def generateDescription(tone,tag,audience,guest,date,time,venue):
    if(tone == "humble"):
        return (f"Respected {markBold(audience)}, We have successfully scheduled {markArticle(tag,False)} meeting with {markBold(guest)} of {markBold(wissenName)}. Below mentioned are the specifics for the same")
    else:
        return (f"{audience} are instructed to join meeting on {utilities.understandDateString(date)}, sharply at {time}, to {venue}.")


def generateTixDescription(description):
    return (f"{markItalic(description)}")


def getDateNow():
    now = datetime.now()
    return clampDate(now)


#returns a list containting three data that is hour, minute, second (Zero Padded)
def getTimeNow():
    now = datetime.now()
    return [now.strftime("%I"),now.strftime("%M"),now.strftime("%S")]


def clampDate(dateString):
    return dateString.strftime("[%d %b \'%y]")

# today : today
# tomorrow : tomorrow
# next X : next X days later

def understandDateString(str):
    tokens = str.lower().split()
    if("today" in tokens):
        return getDateNow()
    elif("tomorrow" in tokens):
        return clampDate(datetime.now()+timedelta(1))         
    elif("next" in tokens):
        return clampDate(datetime.now()+timedelta(int(tokens[1])))
    else:
        return str

def clampTime():
    pass

def markBold(str):
    return f"*{str}*"

def markItalic(str):
    return f"_{str}_"

def markArticle(str,isStart):
    if(str[0] in ['a','e','i','o','u','A','E','I','O','U']):
        if(isStart):
            return f"An {str}"
        else:
            return f"an {str}"
    else:
        if(isStart):
            return f"A {str}"
        else:
            return f"a {str}"
        
def markEmoji(emoji):
    emoCode = f"{emoji.encode('utf-8')}"
    return emoji+emoCode.replace("\\x","%").upper()[2:-1]

def changeFont(str,font_name):
    charSet,numSet,capCharSet = settings.getFontStrings(font_name)
    newStr     = ""
    for character in str:
        if(character >= 'A' and character <= 'Z'):
            newStr += capCharSet[ord(character)-65]
        elif(character >= 'a' and character <= 'z'):
            newStr += charSet[ord(character)-97]
        elif(character >= '0' and character <= '9'):
            newStr += numSet[ord(character)-48]
        else:
            newStr+=character
    return newStr

def validate_mobile_number(mobile_number):
    pattern = re.compile(r'^\d{10}$')
    return bool(pattern.match(mobile_number))

def validate_email_address(str):
    pat = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    if re.match(pat,str):
        return True
    return False


# def understandLocations(str):
#     pass
# #generates address coressponding to the location code
# def generateAddress(loc_code):
#     pass
