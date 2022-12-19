from . import views
from django.urls import path

urlpatterns = [
    path('', views.homePage, name="home"),
    path('circuit/', views.circuitPage, name="circuit"),
    path('miscari-oscilatorii/', views.miscariPage, name="miscari-osilatorii"),
]
