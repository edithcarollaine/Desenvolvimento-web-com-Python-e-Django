from django.shortcuts import render, redirect
from .models import Evento

# Create your views here.

def home(request):
    return redirect('/agenda/')
def lista_evento(request):
    #usuario = request.user
    evento = Evento.objects.all()
    dados = {'eventos': evento}
    return render(request, 'agenda.html', dados)
