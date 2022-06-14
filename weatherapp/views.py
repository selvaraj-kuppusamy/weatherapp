from warnings import catch_warnings
from django.shortcuts import render
import urllib
import json


# Create your views here.
def index(request):
    if request.method == 'POST':
        city = request.POST.get('city')
        city = city.replace(" ", "+")
        api_url = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q='+ city +'&units=metric&appid=e5630b7fcd45cc520fd2e1957b922e1e').read()
        weatherdata = json.loads(api_url)
        city = city.replace("+", " ")
        data = {
            'country': city,
            'weather_description': weatherdata['weather'][0]['description'],
            'weather_temperature': weatherdata['main']['temp'],
            'weather_pressure': weatherdata['main']['pressure'],
            'weather_humidity': weatherdata['main']['humidity'],
            'weather_icon': weatherdata['weather'][0]['icon'],
        }
    else:
        city = None
        data = {
            'country': None,
            'weather_description': None,
            'weather_temperature': None,
            'weather_pressure': None,
            'weather_humidity': None,
            'weather_icon': None,
        }




    return render(request, 'index.html',{"city":city, "data": data})