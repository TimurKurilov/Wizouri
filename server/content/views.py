from django.shortcuts import render
import os 
import requests
from dotenv import load_dotenv

key = os.getenv('API_KEY')

def main_page(request):
    
    return render(request, 'content/main.html')