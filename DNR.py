import requests
import json

url = "https://api-basketball.p.rapidapi.com/odds"

querystring = {"game":"1912"}

headers = {
	"X-RapidAPI-Key": "d8b5e4c393mshdeeb57ca5e71e4dp1a1915jsn2f371c4f6d98",
	"X-RapidAPI-Host": "api-basketball.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

json_obj = response.json()

json_str = json.dumps(json_obj)

print(json_str)


with open("first_odds_request.json", "w") as write_file:
    json.dump(response, write_file)