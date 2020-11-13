import requests

baseUrl = 'http://api.openweathermap.org/data/2.5/weather'
parameters = {
    'id': '5811696',
    'appid': '8bfe5d1cde91330c7c129bb3a505fae1'
}
response = requests.get(baseUrl, params=parameters)
print(response.content)
