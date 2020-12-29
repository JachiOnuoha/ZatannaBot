from dotenv import load_dotenv
import os
load_dotenv()


# Core Configuration (AUTHORIZED PERSONEL ONLY)
HOST = "irc.twitch.tv"
PORT = int(os.getenv("PORT_NUMBER"))
PASS = os.getenv("OAUTH_KEY")
IDENT = os.getenv("BOT_ACCOUNT_NAME")
COMPANYINFO = "This bot is inspired by the Nida_Bot design. It is still a prototype in development by Jachimike Onuoha and Wisdom Orji"
CommandList = " MrDestructoid !dev for Bot info || !spellcast [Phrase] to translate phrase into a Zatanna-like spell || !vote [Name] to vote for daily Team battles || !stats to check Team Battle scores || !vote help for voting info || !boo [NAME] to disrespect || !social for CHANNEL'S social media info"
# Prototype CommandList = ['"!bot dev": Bot info, "!bot uptime": Stream uptime(currently unavailable), "!bot spellcast": translate to zatanna spell, "!bot songreq (SONGNAME)": song request']


# Editable Setting
Channel_Mods = [os.getenv("TARGET_CHANNEL"), "LIST OF CHANNEL MODS"]
CHANNEL = os.getenv("TARGET_CHANNEL")
SOCIAL = "SOCIAL MEDIA INFO"
StreamName = ["LIST OF STREAM TITLES"]
TeamA = "CANDIDATE_A"
TeamB = "CANDIDATE_B"
tagA = "ABRREVIATON OF CANDIDATE A"
tagB = "ABBREVIATION OF CANDIDATE B"
ENTRANCE = " Welcome to " + CHANNEL + "'s " + StreamName[0] + " || Today's Team Battle will be " + TeamA + " vs " + TeamB + " || For bot commands, type !assist "
FARWELL = "bYe eVeRyOnE!!! FutureMan FutureMan FutureMan "
ScoreA = 0
ScoreB = 0
