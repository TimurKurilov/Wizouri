from django.shortcuts import render
from .forms import SearchForm
import requests
from dotenv import load_dotenv
import os
import datetime
from datetime import timedelta

load_dotenv()

# Create your views here.
def weather_search(request):
    form = SearchForm(request.GET)
    weather_data = None
    search = None
    if form.is_valid():
        search = form.cleaned_data.get('query', None)
        if search:
            key = os.getenv('API_KEY')
            api_url = f'http://api.weatherapi.com/v1/current.json?key={key}&q={search}&aqi=no'
            response = requests.get(api_url, verify=False)
            if response.status_code == 200:
                weather_data = response.json()
    return render(request, 'search/weather_results.html', {'form': form, 'weather_data': weather_data, 'search' : search})

def daily_weather(request):
    search = request.GET.get('city')
    weather_data = {}
    now = datetime.datetime.now()
    now = now.strftime("%Y-%m-%d")
    now_day = datetime.datetime.now() + timedelta(days=1)
    now_day = now_day.strftime("%Y-%m-%d")
    if search:
        key = os.getenv('API_KEY2')
        api_url = f'https://api.weatherbit.io/v2.0/history/hourly?city={search}&start_date={now}&end_date={now_day}&key={key}'
        response = requests.get(api_url, verify=False)
        if response.status_code == 200:
                weather_data = response.json()
    return render(request, 'search/daily_weather.html', {'weather_data': weather_data, 'search': search})   
