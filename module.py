import utilities as util
import tickets

## CONSTANTS
FONT1 = ""
FONT2 = "bold-aerial"


# Happy Birthday Wish
# Recruitment Drive Generator
# Organization Wide Share
# Change in Venue
# Bold Points
# Link Share :Trello
# Festival Wishes
# Organization Update
# Position Update and Upgrade
# Festivals Update
# Join our Social Media Page
# 
def generateMeetingUpdate(tokens):
    description,tone,tag,audience,guest,date,time,venue,agenda = tokens
    if(len(description)!=0):
        message = description
    else:
        message = f"""{util.changeFont(util.markBold("!! Meeting Update"),FONT2)} {util.getDateNow()}\n{util.generateDescription(tone,tag,audience,guest,util.understandDateString(date),time,venue)}\n\n{util.markBold("Date")} : {util.understandDateString(date)}\n{util.markBold("Time")} : {time}\n{util.markBold("Venue")} : {venue}\n{util.markBold("Agenda")} : {agenda}\n"""
    return message

def generateTicket(tokens):
    description = tokens[0]
    message = f"""{util.changeFont(util.markBold("!! TICKET UPDATE"),"")} {util.getDateNow()}\n{util.markBold(tickets.generateTixNumber())} - {util.changeFont(util.generateTixDescription(description),"")}\n{util.markBold("Tag : ")}"""
    return message