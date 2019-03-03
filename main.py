import spotipy
from spotipy.oauth2 import SpotifyClientCredentials


def get_formatted_info(spotify_client, input_uri):
    # Get the current track info
    j_results = spotify_client.track(track_id=input_uri)

    # Parse the JSON result
    output_info = '%02d' % track_idx +\
                  ') ' +\
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
                  ']' +\
                  '\n\n'

    return output_info


if __name__ == "__main__":
    # Initialise the Spotipy instance and feed it with the required credentials.
    client_credentials_manager = SpotifyClientCredentials()
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

    # Load the input file
    input_file = open("input.txt", "r")
    input_URIs = input_file.read().splitlines()

    # Open the output file
    output_file = open("output.txt", "w")

    # Init a counter
    track_idx = 1

    # Iterate over all input elements
    uri: str
    for uri in input_URIs:
        # Strip the line endings
        uri.strip("\n")

        # Print the currently processed file
        print("Now loading: " + uri)

        # Parse the JSON result
        output_info = get_formatted_info(sp, uri)

        print(output_info)

        output_file.write(output_info)

        track_idx += 1

    input_file.close()
    output_file.close()
