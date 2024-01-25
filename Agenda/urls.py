from django.contrib import admin
from django.urls import path
from django.urls import include
from AppAgenda import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('AppAgenda.urls')),
]
