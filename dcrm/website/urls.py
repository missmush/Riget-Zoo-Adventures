from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home,name=''),
    path('home', views.home,name='home'),

    path('about', views.about,name='about'),

    path('zoo-booking', views.zoobooking,name='zoo-booking'),

    path('hotel-booking', views.hotelbooking,name='hotel-booking'),

    path('adoption', views.adopt,name='adoption'),

    path('login', views.login,name='login'),
]
