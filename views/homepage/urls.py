from django.urls import path

from views.homepage.views import HomePageViewFunction


urlpatterns = [
    path('', HomePageViewFunction, name='homepage'),
]
