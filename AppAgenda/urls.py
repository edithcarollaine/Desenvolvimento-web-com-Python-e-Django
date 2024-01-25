from django.urls import path
from AppAgenda import views

urlpatterns = [
    path('', views.home),
    path('agenda/', views.lista_evento),
    path('agenda/evento/', views.evento),
    path('agenda/evento/submit', views.submit_evento),
    path('agenda/delete/<int:id_evento>', views.delete_evento),
    path('login/', views.login_user),
    path('login/submit', views.submit_login),
    path('logout/', views.logout_user),
]
