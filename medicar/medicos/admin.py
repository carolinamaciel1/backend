from django.contrib import admin
from django.contrib.admin import ModelAdmin

from medicar.medicos.models import Medico


@admin.register(Medico)
class Medico(ModelAdmin):
    pass
