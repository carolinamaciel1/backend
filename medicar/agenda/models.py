from datetime import date
from django.db import models

from medicar.medicos.models import Medico


class Horario(models.Model):

    def __str__(self):
        return str(self.hora)

    hora = models.TimeField(blank=False, null=False)


class Agenda(models.Model):

    def __str__(self):
        data_agenda = self.medico.nome + ' - ' + str(self.dia)
        return data_agenda

    medico = models.ForeignKey(Medico, max_length=50, on_delete=models.CASCADE, blank=False, null=False)
    dia = models.DateField(blank=False, null=False)
    horarios = models.ManyToManyField(Horario)
