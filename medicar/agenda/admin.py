from django.contrib import admin
from django.contrib.admin import ModelAdmin

from medicar.agenda.models import Agenda, Horario


@admin.register(Agenda)
class Agenda(ModelAdmin):
    pass


@admin.register(Horario)
class Horario(ModelAdmin):
    pass
