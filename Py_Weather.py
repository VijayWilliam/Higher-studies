import requests
api_url_city_state = "api.openweathermap.org/data/2.5/weather?q={city name},{state code}&appid={API key}"
api_url_zip = "api.openweathermap.org/data/2.5/weather?zip={zip code},{country code}&appid={API key}"

str = input("Enter Zip code (OR) City name: ")
if (str.isnumeric() == True):
    print ("Zip code is entered")
else:
    tempState = input("Enter state code: ")
    if (str.isalpha() == True) and (tempState.isalpha() == True):
        print("City and state code entered")
        response = requests.get(api_url_city_state)
    else:
        print("Incorrect City name or state code entered")
        response = requests.get(api_url_zip)
ApiOutput = response.json()
print(ApiOutput)
