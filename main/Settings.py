from dotenv import load_dotenv
import os
load_dotenv()


# Core Configuration (AUTHORIZED PERSONEL ONLY)
HOST = "irc.twitch.tv"
PORT = int(os.getenv("PORT_NUMBER"))
PASS = os.getenv("OAUTH_KEY")
IDENT = os.getenv("BOT_ACCOUNT_NAME")
COMPANYINFO = "This bot is inspired by the Nida_Bot design. It is still a prototype in development by Jach_Imperial"

# Editable Setting
Channel_Mods = [os.getenv("TARGET_CHANNEL"), "LIST OF CHANNEL MODS"]
CHANNEL = os.getenv("TARGET_CHANNEL")
SOCIAL = "SOCIAL MEDIA INFO"
StreamName = "GAME/TOPIC TITLE"
TeamA = "CANDIDATE_A"
TeamB = "CANDIDATE_B"
tagA = "ABRREVIATON OF CANDIDATE A"
tagB = "ABBREVIATION OF CANDIDATE B"
ENTRANCE = " Welcome to " + CHANNEL + "'s " + StreamName + " || Today's Team Battle will be " + TeamA + " vs " + TeamB + " || For bot commands, type !assist "
FARWELL = "bYe eVeRyOnE!!! FutureMan FutureMan FutureMan "
ScoreA = 0
ScoreB = 0
