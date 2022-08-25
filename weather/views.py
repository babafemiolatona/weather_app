# from django.shortcuts import render
# import requests
# from .models import City
# from .forms import CityForm

# def index(request):
#     url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=dc95d38b86072c50bf51e3dce1e3b501'
#     cities = City.objects.all()

#     if request.method == 'POST': # only true if form is submitted
#         form = CityForm(request.POST) # add actual request data to form for processing
#         form.save() # will validate and save if validate

#     form = CityForm()
#     weather_data = []

#     for city in cities:
#         city_weather = requests.get(url.format(cities)).json() #request the API data and convert the JSON to Python data types

#     weather = {
#         'city' : city.name,
#         'temperature' : city_weather['main']['temp'],
#         'description' : city_weather['weather'][0]['description'],
#         'icon' : city_weather['weather'][0]['icon']
#     }

#     weather_data.append(weather)

#     context = {'weather_data' : weather_data, 'form': 'form'}

#     return render(request, 'weather/index.html', context) #returns the index.html template

import requests
from django.shortcuts import render,redirect
from .models import City
from .forms import CityForm

def index(request):

    if request.method == 'POST':
        form = CityForm(request.POST)
        form.save()

    form = CityForm()
    cities = City.objects.all()
    weather_data = []

    for city in cities:
        url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=dc95d38b86072c50bf51e3dce1e3b501'
        r = requests.get(url.format(city.name)).json()

        city_weather = {
            'id' : city.id,
            'city' : r['name'],
            'temperature' : r['main']['temp'],
            'description' : r['weather'][0]['description'],
            'icon' : r['weather'][0]['icon'],
        }

        weather_data.append(city_weather)

    context = {'weather_data' : weather_data, 'form' : form}

    return render(request, 'weather/index.html', context)


def delete(request, id):

    if request.method == 'POST':
        City.objects.filter(id=id).delete()

    return redirect('/')