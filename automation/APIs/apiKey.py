import requests
import hiddenkeys

baseUrl = 'http://api.openweathermap.org/data/2.5/weather'
parameters = {
    'id': '5811696', # Spokane, WA
    'appid': hiddenkeys.get_key()
}
response = requests.get(baseUrl, params=parameters)
print(response.content)
