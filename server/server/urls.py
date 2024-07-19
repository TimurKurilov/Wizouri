from django.contrib import admin
from django.urls import path
from search.views import weather_search

urlpatterns = [
    path('admin/', admin.site.urls),
    path('search/', weather_search, name='weather_search'),
]
