import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# Initialise the Spotipy instance and feed it with the required credentials.
client_credentials_manager = SpotifyClientCredentials()
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# Load the input file
input_file = open(".\\input.txt", "r")
input_URIs = input_file.read().splitlines()

# Iterate over all input elements
uri: str
for uri in input_URIs:
    # Strip the line endings
    uri.strip("\n")

    # Print the currently processed file
    print("Now loading: " + uri)

    # Get the current track info
    j_results = sp.track(track_id=uri)

    # Parse the JSON result
    output_info = '-   ' +\
                  j_results['artists'][0]['name'] +\
                  ' - ' +\
                  j_results['name'] +\
                  '\n' +\
                  '        ' +\
                  j_results['album']['name'] +\
                  ' (' +\
                  j_results['album']['album_type'] +\
                  ') [' +\
                  j_results['album']['release_date'] +\
                  ']'

    print(output_info)
