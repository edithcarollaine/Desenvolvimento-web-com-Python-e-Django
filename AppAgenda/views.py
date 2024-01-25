from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .models import Evento
from django.contrib.auth.decorators import login_required


# Create your views here.

def home(request):
    return redirect('/agenda/')

def login_user(request):
    return render(request, 'login.html')

def logout_user(request):
    logout(request)
    return redirect('/')

def submit_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        usuario = authenticate(username=username, password=password)
        if usuario is not None:
            login(request, usuario)
            return redirect('/')
    else:
        return redirect('/')

@login_required(login_url='/login/')
def lista_evento(request):
    usuario = request.user
    evento = Evento.objects.filter(usuario=usuario)
    dados = {'eventos': evento}
    return render(request, 'agenda.html', dados)
