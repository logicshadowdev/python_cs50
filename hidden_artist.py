import requests
import base64

hidden = "VGhlIFdlZWtuZA=="

def reveal_artist():
    print("🔍  Decoding hidden artist...")
    artist = base64.b64decode(hidden).decode()
    return artist

def search_artist():
    artist = reveal_artist()
    params = {
        "entity": "song",
        "limit": 15,
        "term": artist
    }

    try:
        response = requests.get(
            "https://itunes.apple.com/search",
            params=params
        )
        response.raise_for_status()
        data = response.json()

    except requests.RequestException:
        print("⚠️  Error: Check your internet connection")
        return
    
    print("\n🎵 Artist Revealed:", artist.upper())
    print("-" * 40)

    for i, result in enumerate(data["results"], start=1):
        track = result.get("trackName", "Unknown Track")
        album = result.get("collectionName", "Unknown Album")
        print(f"{i}. {track} | Album: {album}")

    print("_" * 40)

search_artist()