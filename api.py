import requests


url = "https://weatherapi-com.p.rapidapi.com/current.json"

headers = {
		"X-RapidAPI-Key": "7dc783f7c0msh74790f20df568edp13e418jsn7a470f461168",
		"X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com" }

error_message = "N/A"
error_message2 = "City does not exist or you've reached server requests limit"
default_color = "rgb(131, 187, 233)"



class Wheather:
	def __init__(self, name_of_city: str) -> tuple:
		self.name_of_city = name_of_city
		

	def apidata(self) -> tuple:
		
		querystring = {"q":""}
		querystring["q"] = self.name_of_city
		r = requests.request("GET", url, headers=headers, params=querystring)
		data = r.json()
		cityName = data["location"]["name"]
		countryName = data["location"]["country"]
		temperature = data["current"]["temp_c"]
		wind = data["current"]["wind_kph"]
		wheather_condition = data["current"]["condition"]["text"]
		color = self.background_color(wheather_condition)
		print(wheather_condition)
		
		return cityName, countryName, temperature, wind, color


	def background_color(self, wheather_condition: str) -> str:
		if wheather_condition == "Sunny":
			return "yellow"
		elif wheather_condition == "Mist" or wheather_condition == "Fog" or wheather_condition == "Overcast":
			return "grey"
		elif wheather_condition == "Light rain shower" or wheather_condition == "Light rain":
			return "blue"
		elif wheather_condition == "Thunder" or wheather_condition == "Storm" or wheather_condition == "Moderate or heavy rain with thunder":
			return "black"
		elif wheather_condition == "Partly cloudy":
			return "rgb(192, 192, 192)"
		else :
			return default_color



	def error_handler(self) -> tuple:

		try:
			data = self.apidata()
			return data
		except:
			return error_message2, error_message, error_message, error_message, default_color
