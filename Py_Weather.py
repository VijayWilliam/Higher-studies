import requests
import json
#Hardcode variables
API_key = "680dd03f84541ec42a0f6c434c4c237e"
country_code = "US"
zip_code = ""
city_name = ""
state_code = ""

def check_response(response):
    if response.status_code == 200:
        ApiOutput = response.json()
        main = ApiOutput['main']
        temperature = main['temp']
        city_name = ApiOutput['name']
        print(f"{city_name} current temperature is {temperature}")
    else:
        print("Bad return from Openweather API")

#Get input from user
str_input = input("Enter Zip code (OR) City name: ")
temp_units = input("You want temperature in Celcius (C) or Fahrenheit (F)? ")

if temp_units == "C":
    units = "metric"
elif temp_units == "F":
    units = "imperial"
else:
    print("Invalid temperature units entered")
    quit()

#Send HTTP API request based on user entry. If entry is not good, send error message
if (str_input.isnumeric() == True):
    zip_code = str_input
    api_url_zip = "http://api.openweathermap.org/data/2.5/weather?zip="+zip_code+","+country_code+"&appid="+API_key+"&units="+units    
    response = requests.get(api_url_zip)
    check_response(response)
else:
    city_name = str_input 
    state_code = input("Enter state code: ")
    if (city_name.isalpha() == True) and (state_code.isalpha() == True):
        api_url_city_state = "http://api.openweathermap.org/data/2.5/weather?q="+city_name+","+state_code+","+country_code+"&appid="+API_key+"&units="+units
        response = requests.get(api_url_city_state)
        check_response(response)
    else:
        print("Incorrect City name or state code entered")
