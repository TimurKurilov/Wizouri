from django.contrib import admin
from django.urls import path
from search.views import weather_search, daily_weather
from content.views import main_page
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_page, name='main'),
    path('search/', weather_search, name='weather_search'),
    path('search/daily/', daily_weather, name='daily_weather'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    