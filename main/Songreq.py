# Manages song request features
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Access to environment variables
from dotenv import load_dotenv
import os
load_dotenv()

scope_queue = "streaming"
scope_currPlaying = "user-read-currently-playing"

# These are the SpotipyOAUTH object that will be used to manage authorization and make API calls
sp_1 = SpotifyOAuth(
        client_id=os.getenv("SPOTIPY_CLIENT_ID"),
        client_secret=os.getenv("SPOTIPY_CLIENT_SECRET"),
        redirect_uri=os.getenv("SPOTIPY_REDIRECT_URI"),
        state="code",
        scope=scope_currPlaying)


def authorizeSongReq():
    authCode = sp_1.get_authorization_code()
    accessToken = sp_1.get_access_token(authCode, as_dict=False)
    print(accessToken)


authorizeSongReq()

songRequest = spotipy.Spotify(auth_manager=sp_1)

trackData = songRequest.currently_playing(market="US")
trackName = trackData['item']['name']
artistName = trackData['item']['artists'][0]['name']
print("Song: {}".format(trackName))
print("Artist(s): {}".format(artistName))
