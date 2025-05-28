import requests
import json


def getDisneyCharacter(name=None):
    """
    Get Disney character info using Disney API.
    If name is provided, it filters the character list.
    """
    url = "https://api.disneyapi.dev/character"
    if name:
        url += f"?name={name}"
    response = requests.get(url)
    if response.status_code != 200:
        return f"Failed to fetch Disney character data. Status code: {response.status_code}"
    
    data = response.json()
    if not data.get("data"):
        return "No character data found."
    
    character = data["data"][0]
    character_info = {
        "name": character.get("name"),
        "films": character.get("films"),
        "tvShows": character.get("tvShows"),
        "videoGames": character.get("videoGames"),
        "allies": character.get("allies"),
        "enemies": character.get("enemies"),
    }
    return json.dumps(character_info, indent=4)



print("\n== Disney Character Info ==")
print(getDisneyCharacter("Mickey Mouse"))
