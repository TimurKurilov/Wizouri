from django.shortcuts import render
import os
import requests
from django.views.decorators.cache import cache_page
from dotenv import load_dotenv

load_dotenv()  # Загружаем переменные окружения из .env файла

key = os.getenv('API_KEY')

def get_weather(url):
    response = requests.get(url)
    print(f'Request URL: {url}')
    if response.status_code == 200:
        return response.json()
    else:
        print(f'Ошибка: {response.status_code}')
    return None
@cache_page(60 * 1)
def main_page(request):
    new_york_weather = get_weather(f'https://api.weatherapi.com/v1/current.json?key={key}&q=new-york&aqi=no')
    moscow_weather = get_weather(f'https://api.weatherapi.com/v1/current.json?key={key}&q=moscow&aqi=no')
    beijing_weather = get_weather(f'https://api.weatherapi.com/v1/current.json?key={key}&q=beijing&aqi=no')
    warsaw_weather = get_weather(f'https://api.weatherapi.com/v1/current.json?key={key}&q=warsaw&aqi=no')
    rome_weather = get_weather(f'https://api.weatherapi.com/v1/current.json?key={key}&q=rome&aqi=no')
    berlin_weather = get_weather(f'https://api.weatherapi.com/v1/current.json?key={key}&q=berlin&aqi=no')
    tokyo_weather = get_weather(f'https://api.weatherapi.com/v1/current.json?key={key}&q=tokyo&aqi=no')
    paris_weather = get_weather(f'https://api.weatherapi.com/v1/current.json?key={key}&q=paris&aqi=no')
    oslo_weather = get_weather(f'https://api.weatherapi.com/v1/current.json?key={key}&q=oslo&aqi=no')
    bern_weather = get_weather(f'https://api.weatherapi.com/v1/current.json?key={key}&q=bern&aqi=no')
    astana_weather = get_weather(f'https://api.weatherapi.com/v1/current.json?key={key}&q=astana&aqi=no')
    washington_weather = get_weather(f'https://api.weatherapi.com/v1/current.json?key={key}&q=washington&aqi=no')
    ottawa_weather = get_weather(f'https://api.weatherapi.com/v1/current.json?key={key}&q=ottawa&aqi=no')
    london_weather = get_weather(f'https://api.weatherapi.com/v1/current.json?key={key}&q=london&aqi=no')
    cleveland_weather = get_weather(f'https://api.weatherapi.com/v1/current.json?key={key}&q=cleveland&aqi=no')

    context = {
        'new_york_weather': new_york_weather,
        'moscow_weather': moscow_weather,
        'beijing_weather': beijing_weather,
        'warsaw_weather': warsaw_weather,
        'rome_weather': rome_weather,
        'berlin_weather': berlin_weather,
        'tokyo_weather': tokyo_weather,
        'paris_weather': paris_weather,
        'oslo_weather': oslo_weather,
        'bern_weather': bern_weather,
        'astana_weather': astana_weather,
        'washington_weather': washington_weather,
        'ottawa_weather': ottawa_weather,
        'london_weather': london_weather,
        'cleveland_weather': cleveland_weather,
    }

    return render(request, 'content/main.html', context)
