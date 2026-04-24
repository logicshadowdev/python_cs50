"""
import json
import requests
import sys

if len(sys.argv) != 2:
    sys.exit("Please input the artist name.")

response = requests.get("https://itunes.apple.com/search?entity=song&limit=50&term=" + sys.argv[1])

o = response.json()
for result in o["results"]:
    print(result["trackName"])
"""
import json
import requests
import sys

if len(sys.argv) < 2:
    sys.exit("Please input the artist name.")

artist = " ".join(sys.argv[1:])

params = {
    "entity": "song",
    "limit": 60,
    "term": artist
}
response = requests.get("https://itunes.apple.com/search", params=params)

o = response.json()
for result in o["results"]:
    print(result["trackName"])