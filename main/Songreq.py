# Manages song request features
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Access to environment variables
from dotenv import load_dotenv
import os
load_dotenv()

scope_queue = "streaming"
scope_currPlaying = "user-read-currently-playing"

# These are the SpotipyOAUTH object that will be used to manage authorization
# and make API calls
sp_currPlaying = SpotifyOAuth(
        client_id=os.getenv("SPOTIPY_CLIENT_ID"),
        client_secret=os.getenv("SPOTIPY_CLIENT_SECRET"),
        redirect_uri=os.getenv("SPOTIPY_REDIRECT_URI"),
        state="code",
        scope=scope_currPlaying)


def authorizeSongReq():
    authCode_currplaying = sp_currPlaying.get_authorization_code()
    sp_currPlaying.get_access_token(authCode_currplaying, as_dict=False)


# Get currently playing track of stream
def getCurPlaying():
    songRequest_currPlaying = spotipy.Spotify(auth_manager=sp_currPlaying)
    trackData = songRequest_currPlaying.currently_playing(market="US")
    if (trackData is not None):
        trackName = trackData['item']['name']
        artistName = trackData['item']['artists'][0]['name']
        return("Song: {} || Artist(s): {}".format(trackName, artistName))
    else:
        return("Please try again later ThankEgg")
