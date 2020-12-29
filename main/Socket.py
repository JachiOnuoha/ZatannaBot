import socket
from Settings import HOST, PORT, PASS, IDENT, CHANNEL
import sys


# Connect to Twitch and join your stream
def openSocket():

    s = socket.socket()
    s.connect((HOST, PORT))
    s.send(("PASS {}\r\n".format(PASS)).encode("UTF-8"))  # s.send("PASS " + PASS + "\r\n")
    s.send(("NICK {}\r\n".format(IDENT)).encode("UTF-8"))  # s.send("NICK " + IDENT + "\r\n")
    s.send(("JOIN #{}\r\n".format(CHANNEL)).encode("UTF-8"))  # s.send("JOIN # " + CHANNEL + "\r\n")
    return s


def sendMessage(s, message):
    messageTemp = "PRIVMSG #" + CHANNEL + " :" + message
    s.send((messageTemp + "\r\n").encode("UTF-8"))
    print("Sent: " + messageTemp)
