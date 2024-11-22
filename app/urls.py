from django.urls import path, include
from . import views

urlpatterns = [
  path('', views.index, name="index"),
  path('ranking/', views.ranking, name="ranking"),
  path('game/', views.game, name="game"),
  
  path('get/', views.get, name="get"),
  path('add/', views.add, name="add")
]