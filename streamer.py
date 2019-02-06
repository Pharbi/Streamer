import spotipy
import sys
import spotipy.util as util
import os
import webbrowser
from config import Config

scope = 'user-read-playback-state'

twy = 'spotify:artist:0nq64XZMWV1s7XHXIkdH7K'

env_obj = Config()

def getStream(username):

    token = util.prompt_for_user_token(username, scope=scope, client_id=env_obj.cli_id, client_secret=env_obj.cli_secret, redirect_uri = env_obj.redirect_uri)

    if token:
        sp = spotipy.Spotify(auth=token)
        playlists = sp.user_playlists(username)
        res = sp.artist_albums(twy, album_type='album')
        albums = res['items']
        topT = sp.artist_top_tracks(twy)

        for track in topT['tracks'][:3]:
            print('audio : ' + track['preview_url'])
            lastTrack = track['preview_url']

        print(lastTrack)
        openBrowser(lastTrack)
        while res['next']:
            res = spotipy.next(res)
            albums.extended(res['items'])

        for album in albums:
            print(album['name'])
    return lastTrack

def openBrowser(url):
    #Currently going to hard code a html file and then 'open' it to stream the track
    html = """
    <!DOCTYPE html>
    <html>
        <head>
            <Title> Streaming window </Title>
            <script type="text/javascript" src="./index.js">
             </script>
        </head>
        <body onload="startStreamFunction('http://localhost:8808')">
            <audio autoplay="autoplay" controls="controls">
            <!-- I'm so so sorry about this autoplay -->
                <source src=%s type="audio/mpeg">
                <p>If you can read this, your browser does not support the audio element.</p>
            </audio>
        </body>
    </html>
    """ % (url, url)

    path = os.path.abspath('index.html')
    actual_url = "file://" + path

    with open(path, 'w') as f:
        f.write(html)
    webbrowser.open(actual_url)

if __name__ == "__main__":
    if len(sys.argv) > 1:
       username = sys.argv[1]
    else:
         print("Usage: %s username" % (sys.argv[0],))
         sys.exit()
    url = getStream(username)
