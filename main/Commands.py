import math
import datetime


def getUser(line):
    seperate = line.split(":", 2)
    user = seperate[1].split("!", 1)[0]
    return user


def getMessage(line):
    seperate = line.split(":", 2)
    message = seperate[2]
    return message


def spellcast(line):
    seperate = line.split("spellcast", 2)
    message = seperate[1]
    text = message[::-1]
    if len(text) < 12:  # Use 12 because the program adds two to the length of the string
        text = text.upper()
    return text


def boo(line):
    seperate = line.split("boo", 2)
    message = seperate[1]
    text = "trash " + message
    # if len(text) < 12:  # Use 12 because the program adds two to the actual length of the string
    text = text.upper()
    return text


def uptime(startTime):
    uptime = datetime.datetime.now()
    uptime = uptime - startTime
    time = str(uptime).split(':')
    print(type(time[2]))
    time[0] = str(int(math.floor(float(time[0]))))
    time[1] = str(int(math.floor(float(time[1]))))
    time[2] = str(int(math.floor(float(time[2]))))
    if(int(time[0]) <= 0):
        return(time[1] + ' minutes and ' + time[2] + ' seconds')
    else:
        return(time[0] + ' hours ' + time[1] + ' minutes and ' + time[2] + ' seconds')
