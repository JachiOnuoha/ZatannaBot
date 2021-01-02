import string
from Commands import getUser, getMessage, spellcast, boo, uptime
from Socket import openSocket, sendMessage
from Initialize import joinRoom
from Settings import *
import time
import sys
import datetime
from Songreq import getCurPlaying

# Open the connection socket
s = openSocket()

# Run initiliazation function to connect to the Twitch IRC and SongRequest endpoint
joinRoom(s)

# Store the stream start time
begin = datetime.datetime.now()

readbuffer_join = ""
poll = "open"
while True:
    try:
        readbuffer_join = readbuffer_join + s.recv(1024).decode("UTF-8")
        temp = readbuffer_join.split("\n")
        readbuffer_join = temp.pop()

    except TimeoutError:
        print("PROBLEM")

    for line in temp:
        print(line)
        if "PING :tmi.twitch.tv" in line:
            s.send("PONG :tmi.twitch.tv\r\n".encode())
            break

        user = getUser(line)
        message = getMessage(line)
        print(user + " typed : " + message)
        message = message.lower()

        if "Forza" in message:
            sendMessage(s, "Lightning")
            break

        if "!dev" in message:
            sendMessage(s, COMPANYINFO)
            time.sleep(1)

        elif "!assist" in message:
            sendMessage(s, CommandList)
            time.sleep(1)

        # elif "!bot uptime" in message:
            # sendMessage(s, "currently unavailable")

        elif "!spellcast" in message:
            text = spellcast(message)
            sendMessage(s, " LUL LUL LUL " + text)
            time.sleep(1)

        elif "!boo" in message:
            text = boo(message)
            sendMessage(s, " UnSane UnSane " + text)
            time.sleep(1)

        elif "!social" in message:
            sendMessage(s, "Follow us on Twitter " + SOCIAL)
            time.sleep(1)

        elif "!nowplaying" in message:
            songinfo = getCurPlaying()
            sendMessage(s, songinfo)
            time.sleep(1)

        elif ("!vote" in line):
            if (poll == "open"):
                if (tagA in line) or (TeamA in line):
                    ScoreA += 1
                    sendMessage(s, " CurseLit CurseLit " + user + " voted for " + TeamA)
                    time.sleep(1)
                elif (tagB in line) or (TeamB in line):
                    ScoreB += 1
                    sendMessage(s, " TwitchLit TwitchLit " + user + " voted for " + TeamB)
                    time.sleep(1)
                elif "help" in line:
                    text = " CurseLit TwitchLit Use " + tagA + " to vote for " + TeamA + " and " + tagB + " to vote for " + TeamB
                    sendMessage(s, text)
                    time.sleep(1)
                else:
                    sendMessage(s, "Incorrect Command BibleThump BibleThump ")
                    time.sleep(1)
            else:
                sendMessage(s, "Voting is closed VoteNay VoteNay")
                time.sleep(1)

        elif "!scores" in message:
            text = TeamA + ": " + str(ScoreA) + "  vs " + TeamB + ": " + str(ScoreB)
            print(text)
            sendMessage(s, text)
            time.sleep(1)

    # MOD SPECIFIC COMMANDS
        elif user in Channel_Mods:
            if "!endpoll" in line:
                poll = "closed"
                if ScoreA > ScoreB:
                    sendMessage(s, TeamA + " WON!! Poooound Poooound Poooound ")
                elif ScoreB > ScoreA:
                    sendMessage(s, TeamB + " WON!!! Poooound Poooound Poooound ")

                else:
                    sendMessage(s, "IT'S A TIE PogChamp PogChamp PogChamp")

            # elif "!purge" in line:
                # refreshChat(s)

            elif "!breaktime" in line:
                sendMessage(s, "We'll be back shortly imGlitch imGlitch imGlitch ")

            elif "!relive" in line:
                sendMessage(s, "WE'RE BACK PEOPLE!! KAPOW KAPOW")

            elif "!endstream" in line:
                time.sleep(1)
                sendMessage(s, FARWELL)
                print("Bot effectively closed")
                sys.exit()

            elif "!uptime" in line:
                myTime = uptime(begin)
                sendMessage(s,  'DrinkPurple ' + myTime + ' DrinkPurple')
