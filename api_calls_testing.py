import requests
import json


if __name__ == "__main__":
    

	print("This script will give you the highest combined score of any season(s) from the NBA. It will return the Season, the Teams (the game), the date, the individual scores, and the combined score")

	#if the wrong form/type of input is entered, the script will fail
	
	

	url = "https://free-nba.p.rapidapi.com/games"


	querystring = {"page":"0","per_page":"1300", "Seasons":"2018"}

	headers = {
		"X-RapidAPI-Key": "d8b5e4c393mshdeeb57ca5e71e4dp1a1915jsn2f371c4f6d98",
		"X-RapidAPI-Host": "free-nba.p.rapidapi.com"
	}

	response = requests.get(url, headers=headers, params=querystring)


	decoded_json = response.json(	)
	json_str = json.dumps(decoded_json)


	with open("nba_games.json", "w") as write_file:
		json.dump(decoded_json, write_file, sort_keys=True, indent=4)

	temp_max = 0
	temp_index = None
	for i, ele in enumerate(decoded_json["data"]):

		temp_combo = ele["home_team_score"]+ ele["visitor_team_score"]

		if(temp_combo > temp_max):
			temp_max = temp_combo
			temp_index = i

	home = decoded_json["data"][temp_index]["home_team"]["full_name"]
	away = decoded_json["data"][temp_index]["visitor_team"]["full_name"]
	home_score = decoded_json["data"][temp_index]["home_team_score"]
	away_score = decoded_json["data"][temp_index]["visitor_team_score"]
	
	
	print(f"\n\nIn the 2018 Season, the highest scoring game was between the {home} with {home_score} points, and the {away} with {away_score} points. The combined score was {temp_max}. ")






