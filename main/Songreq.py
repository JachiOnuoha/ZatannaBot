# Manages song request features
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Access to environment vaariables
from dotenv import load_dotenv
import os
load_dotenv()

scope_queue = "streaming"
scope_currPlaying = "user-read-currently-playing"
