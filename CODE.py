import requests

api_key="90ec3131fcb7c4bc506dcbe49929018e"

base="https://api.openweathermap.org/data/2.5/weather?"

city=input("Enter city name:")

complete=base+"appid="+api_key+"&q="+city

response=requests.get(complete).json()

format_data=response['weather'][0]['main']
desc=response['main']
print(format_data)
print(desc)



