# Manages song request features
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Access to environment vaariables
from dotenv import load_dotenv
import os
load_dotenv()

scope_queue = "streaming"
scope_currPlaying = "user-read-currently-playing"

# This is the SpotipyOAUTH object that will be used to manage authorization and make API calls
sp = SpotifyOAuth(
        client_id=os.getenv("SPOTIPY_CLIENT_ID"),
        client_secret=os.getenv("SPOTIPY_CLIENT_SECRET"),
        redirect_uri=os.getenv("SPOTIPY_REDIRECT_URI"),
        state="code",
        scope=scope_currPlaying)


def authorizeSongReq():
    authCode = sp.get_authorization_code()
    accessToken = sp.get_access_token(authCode, as_dict=False)
    print(accessToken)


authorizeSongReq()
