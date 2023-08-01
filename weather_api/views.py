from django.shortcuts import render
import requests

# Create your views here.


def index(request):
    api_url = 'http://api.openweathermap.org./data/2.5/weather?appid=0c42f7f6b53b244c78a418f4f181282a&q='
    city = 'cairo'
    url = api_url + city

    respone = requests.get(url)
    object_content = respone.json()
    city_info = {
        'name': object_content.name,
        'country': object_content['sys']['country'],
        'temperature': object_content['main']['temp'],
        'description': object_content['weather']['0']['description'],
        'icon': object_content['weather']['0']['icon'],
    }
    
    return render(request,'weather.html',{'city_info':city_info})
