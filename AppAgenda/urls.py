from django.urls import path
from AppAgenda import views

urlpatterns = [
    path('agenda/', views.lista_evento),
    path('', views.home),
    path('login/', views.login_user),
    path('login/submit', views.submit_login),
    path('logout/', views.logout_user),
]
