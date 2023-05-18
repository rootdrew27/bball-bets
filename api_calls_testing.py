import requests
import json


if __name__ == "__main__":
    

	print("This script will give you the highest combined score of any season(s) from the NBA. It will return the Season, the Teams (the game), the date, the individual scores, and the combined score")

	#if the wrong form/type of input is entered, the script will fail
	seasons = input("Enter the season(s) as a comma seperated list (eg. 2018, 2020, 2021): ")
	

	url = "https://free-nba.p.rapidapi.com/games"


	querystring = {"page":"0","per_page":"25", "Seasons":f"{seasons}"}

	headers = {
		"X-RapidAPI-Key": "d8b5e4c393mshdeeb57ca5e71e4dp1a1915jsn2f371c4f6d98",
		"X-RapidAPI-Host": "free-nba.p.rapidapi.com"
	}

	response = requests.get(url, headers=headers, params=querystring)


	json_obj = response.json()
	json_str = json.dumps(json_obj, sort_keys=True, indent=4)

	print(json_str)


	# with open("nba_games.json", "w") as write_file:
	# 	json.dump(json_obj, write_file)



