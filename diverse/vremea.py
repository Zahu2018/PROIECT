import requests

city = input('enter the city ')
api = "https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=06c921750b9a82d8f5d1294e1586276f"

json_data = requests.get(api).json()

temp = int(json_data['main']['temp'] - 273.15)

pressure = json_data['main']['pressure']
humidity = json_data['main']['humidity']
wind = json_data['wind']['speed']


    
print('The temperature is:',temp)
print('Presure is:',pressure)
print('Humidity is:',humidity)
print('Wind speed is',wind)