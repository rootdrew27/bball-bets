import requests
import json

url = "https://free-nba.p.rapidapi.com/games"

querystring = {"page":"0","per_page":"25"}

headers = {
	"X-RapidAPI-Key": "d8b5e4c393mshdeeb57ca5e71e4dp1a1915jsn2f371c4f6d98",
	"X-RapidAPI-Host": "free-nba.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)


json_obj = response.json()
json_str = json.dumps(json_obj)


with open("nba_games.json", "w") as write_file:
    json.dump(json_obj, write_file)
