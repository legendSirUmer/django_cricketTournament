"""
URL configuration for django_cricketTournament project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name='index'),
    path('contact/', contact, name='contact'),
    path('matches/', matches, name='matches'),
    path('teams/', teams, name='teams'),
    path('live-score/<int:match_id>/',live_score, name='live_score'),
    path('matchdetails', match_details, name='match_details'),
]


