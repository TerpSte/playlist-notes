import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import argparse


def get_formatted_info(spotify_client, input_uri):
    # Get the current track info
    j_results = spotify_client.track(track_id=input_uri)

    # Create a list with all artists' names
    artists_list = [(j_results['artists'][i]['name'] + '; ') for i in range(len(j_results['artists']))]
    artists_list[-1] = artists_list[-1][:-2]

    # Parse the JSON result
    output_info = '%02d' % track_idx +\
                  ') ' +\
                  ''.join(artists_list) +\
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
    parser = argparse.ArgumentParser(description='Load a Spotify playlist and retrieve some useful info from it.')
    parser.add_argument('input_file', metavar='in', type=str,
                        help='The input file that contains a list with Spotify URIs, onr for each playlist track.')
    parser.add_argument('output_file', metavar='out', type=str,
                        help='The output file. The script will write the retrieved info there.')
    args = parser.parse_args()

    # Initialise the Spotipy instance and feed it with the required credentials.
    client_credentials_manager = SpotifyClientCredentials()
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

    # Load the input file
    input_file = open(args.input_file, "r")
    input_URIs = input_file.read().splitlines()

    # Open the output file
    output_file = open(args.output_file, "w")

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
