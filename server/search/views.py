from django.shortcuts import render
from .forms import SearchForm
import requests
from dotenv import load_dotenv
import os

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
            response = requests.get(api_url)
            if response.status_code == 200:
                weather_data = response.json()
    return render(request, 'search/weather_results.html', {'form': form, 'weather_data': weather_data, 'search' : search})






