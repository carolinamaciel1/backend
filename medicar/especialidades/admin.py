from django.contrib import admin
from django.contrib.admin import ModelAdmin

from medicar.especialidades.models import Especialidade


@admin.register(Especialidade)
class Especialidade(ModelAdmin):
    pass
