# Manages song request features
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Access to environment variables
from dotenv import load_dotenv
import os
load_dotenv()

scope_songReq = "user-read-currently-playing user-modify-playback-state"

# These are the SpotipyOAUTH object that will be used to manage authorization
# and make API calls
sp_songReq = SpotifyOAuth(
        client_id=os.getenv("SPOTIPY_CLIENT_ID"),
        client_secret=os.getenv("SPOTIPY_CLIENT_SECRET"),
        redirect_uri=os.getenv("SPOTIPY_REDIRECT_URI"),
        state="code",
        scope=scope_songReq)


# Get authorization code and access code for SongRequest
def authorizeSongReq():
    authCode_songReq = sp_songReq.get_authorization_code()
    sp_songReq.get_access_token(authCode_songReq, as_dict=False)


# Get currently playing track of stream
def getCurrPlaying():
    songRequest_songReq = spotipy.Spotify(auth_manager=sp_songReq)
    trackData = songRequest_songReq.currently_playing(market="US")
    if (trackData is not None):
        trackName = trackData['item']['name']
        artistName = trackData['item']['artists'][0]['name']
        return("Song: {} || Artist(s): {}".format(trackName, artistName))
    else:
        return("Please try again later ThankEgg")


# Play next track in the queue
def nextTrack():
    # TODO: Handle exception
    songRequest_songReq = spotipy.Spotify(auth_manager=sp_songReq)
    songRequest_songReq.next_track()


# Play previous track in the queue
def prevTrack():
    # TODO: Handle exception
    songRequest_songReq = spotipy.Spotify(auth_manager=sp_songReq)
    songRequest_songReq.previous_track()
