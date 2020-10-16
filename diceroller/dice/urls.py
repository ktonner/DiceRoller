from django.urls import path
from django.urls import include, path

from . import views

# localhost:8000/dice/2
urlpatterns = [
    path('', views.index, name='index'),
    path('dice/', views.rollPage, name='roll'),
    path('<int:number>/',views.rollMany, name="results")
]