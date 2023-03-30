import utilities
import tokenGen as tg

def generateTixNumber():
    timeArray = utilities.getTimeNow()
    date = utilities.getDateNow()[1:3]
    return str(timeArray[0])+str(timeArray[1])+str(date)