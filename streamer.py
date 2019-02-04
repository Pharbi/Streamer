import spotipy
import sys
import pprint
import spotipy.util as util
import os

scope = 'user-library-read'

twy = 'spotify:artist:0nq64XZMWV1s7XHXIkdH7K'
#spotify = spotipy.Spotify()

#spotify.user('gambinooverwatch')
#res = spotify.artist_albums(twy, album_type='album')
#albums = res['items']

#util.prompt_for_user_token(username,scope,client_id='your-app-redirect-url',client_secret='your-app-redirect-url',redirect_uri='your-app-redirect-url')

#token = util.prompt_for_user_token('gambinooverwatch', scope, client_id='http://localhost/', client_secret='http://localhost/', redirect_uri='http://localhost/')
#spotify.Spotify(auth=token)

if len(sys.argv) > 1:
    username = sys.argv[1]
else:
    print("Usage: %s username" % (sys.argv[0],))
    sys.exit()

cli_id = os.environ['CLI_ID']
print(cli_id)
cli_secret = os.environ['CLI_SEC']
redir = os.environ['REDIRECT_URI']

token = util.prompt_for_user_token(username, scope=scope, client_id=cli_id, client_secret=cli_secret, redirect_uri = redir)

if token:
    sp = spotipy.Spotify(auth=token)
    playlists = sp.user_playlists(username)
    res = sp.artist_albums(twy, album_type='album')
    albums = res['items']

    while res['next']:
        res = spotipy.next(res)
        albums.extended(res['items'])

    for album in albums:
        print(album['name'])
