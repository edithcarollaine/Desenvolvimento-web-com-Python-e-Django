from .models import Evento
from django.contrib import admin

# Register your models here.


class EventoAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'data_evento', 'data_criacao')


admin.site.register(Evento, EventoAdmin)