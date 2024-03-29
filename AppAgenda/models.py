from datetime import datetime, timedelta

from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Evento(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)
    data_evento = models.DateTimeField(verbose_name='Data do Evento')
    data_criacao = models.DateTimeField(auto_now=True, verbose_name='Data de Criação')

    class Meta:
        db_table = 'Evento'

    def __str__(self):
        return self.titulo

    def get_data_input_evento(self):
        return self.data_evento.strftime ('%Y-%m-%dT%H:%M')

    def get_evento_atrasado(self):
        if self.data_evento < datetime.now():
            return True
        else:
            return False
