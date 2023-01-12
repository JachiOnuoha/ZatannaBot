
import string
from Socket import sendMessage
from Settings import ENTRANCE, IDENT, CHANNEL
import sys
from Songreq import authorizeSongReq


def joinRoom(s):
    # Connect to Twitch IRC
    readbuffer_join = ""
    Loading = True
    while Loading:
        try:
            readbuffer_join = readbuffer_join + s.recv(1024).decode("UTF-8")
            temp = readbuffer_join.split("\n")
            readbuffer_join = temp.pop()

            for line in temp:
                print(line)
                if("End of /NAMES list" in line):
                    Loading = False
                    print("Passed")
        except TimeoutError:
            print("Problem")
    sendMessage(s, " imGlitch " + ENTRANCE)
    print(IDENT + " has joined " + CHANNEL)

    # Initializa song request features
    authorizeSongReq()
