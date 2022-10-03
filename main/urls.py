from django.urls import path
from unicodedata import name
from django.conf.urls import url
from . import views

urlpatterns = [

    path('', views.main, name='main'),
    path('test', views.test, name='test'),
    path('play', views.play, name='play'),
]