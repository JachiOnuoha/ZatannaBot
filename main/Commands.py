import math
import datetime


# Gets the username of chat members
def getUser(line):
    seperate = line.split(":", 2)
    user = seperate[1].split("!", 1)[0]
    return user


# Gets the message from chat
def getMessage(line):
    seperate = line.split(":", 2)
    message = seperate[2]
    return message


# Reverses any phrase invoked alongsid the command
def spellcast(line):
    seperate = line.split("spellcast", 2)
    message = seperate[1]
    text = message[::-1]
    if len(text) < 12:  # Use 12 because the program adds two to the length of the string
        text = text.upper()
    return text


# Taunts any name of phrase invoked alongside the command
def boo(line):
    seperate = line.split("boo", 2)
    message = seperate[1]
    text = "trash " + message
    # if len(text) < 12:  # Use 12 because the program adds two to the actual length of the string
    text = text.upper()
    return text


# Tells users how long bot has been active
def uptime(startTime):
    uptime = datetime.datetime.now()
    uptime = uptime - startTime
    time = str(uptime).split(':')
    time[0] = str(int(math.floor(float(time[0]))))
    time[1] = str(int(math.floor(float(time[1]))))
    time[2] = str(int(math.floor(float(time[2]))))
    if(int(time[0]) <= 0):
        return(time[1] + ' minutes and ' + time[2] + ' seconds')
    else:
        return(time[0] + ' hours ' + time[1] + ' minutes and ' + time[2] + ' seconds')
