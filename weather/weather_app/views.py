from django.shortcuts import render
from . import views
from .models import City
import requests
from .forms import CityForm

def index(request):
    url='https://samples.openweathermap.org/data/2.5/weather?id=2172797&appid=439d4b804bc8187953eb36d2a8c26a02'
    cities=City.objects.all()

    if request.method=="POST":
        print(request.POST)
        form=CityForm(request.POST)
        form.save()

    form=CityForm()

    weather_data=[]
    for city in cities:
        r=requests.get(url.format(city)).json()
        city_weather={
        'city':city.name,
        'tempreture':r['main']['temp'],
        'description' :r['weather'][0]['description'],
        'icon':r['weather'][0]['icon']
        }
        weather_data.append(city_weather)

    # print(city_weather)
    context={
    'weather_data':weather_data,
    'form':form
    }

    return render(request,'weather_app/base.html',context)
