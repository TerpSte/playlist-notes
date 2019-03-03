# playlist-notes

Convert a Spotify list of tracks to a text list, including various track info (e.g. album, year, etc).

version **0.1.0**

## Intro
Welcome to plylist-notes repo. It contains python tools to easily convert a Spotify plylist into a convenient text list. The output list also contains other useful info, like the album name and the release date.

## Dependecies
The main dependecy of the script, is the Spotipy library, a Python client for the The Spotify Web API, which you can find [here](https://github.com/plamere/spotipy). The documentation of the Spotipy library can be found [here](https://spotipy.readthedocs.io/en/latest/).

Apart from installing the dependency, you will also have to set some environment variables, in order to use this script. These variables contain the Spotify Client ID and Spotify Client Secret, and are mandatory from the Spotify API, in order to make authorised requests. For more info on these concepts, please refer to the Spotify API guide [here](https://developer.spotify.com/documentation/general/guides/authorization-guide/), as well as the Spotipy docs.

Copying from the Spotipy docs, you need to declare the following variables:
```
export SPOTIPY_CLIENT_ID='your-spotify-client-id'
export SPOTIPY_CLIENT_SECRET='your-spotify-client-secret'
```

## Usage
After setting up the dependecies, the usage is simple. Create a text file containing a list of the plylist tracks' URIs and pass it into the python script, along with the path of the output file:
```
python get_info_from_list.py input.txt output.txt [-v]
```