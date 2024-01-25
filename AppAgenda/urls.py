from django.urls import path
from AppAgenda import views

urlpatterns = [
    path('agenda/', views.lista_evento),
    path('', views.home),
]
