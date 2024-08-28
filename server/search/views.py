from django.shortcuts import render
from .forms import SearchForm
import requests
from dotenv import load_dotenv
import os

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
    if search:
        key = os.getenv('API_KEY2')
        api_url = f'https://api.weatherbit.io/v2.0/forecast/daily?city={search}&key={key}'
        response = requests.get(api_url, verify=False)
        if response.status_code == 200:
                weather_data = response.json()
    return render(request, 'search/daily_weather.html', {'weather_data': weather_data, 'search': search})
