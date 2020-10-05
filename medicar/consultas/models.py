from django.db import models
from medicar.agenda.models import Agenda
from medicar.agenda.models import Horario
from medicar.users.models import UsuarioCustomizado


class Consulta(models.Model):
    def __str__(self):
        data_consulta = self.agenda.medico.nome + '-' + str(self.horario)
        return data_consulta

    horario = models.ForeignKey(Horario, on_delete=models.DO_NOTHING, null=False)
    data_agendamento = models.DateField(auto_now=True, null=False)
    agenda = models.ForeignKey(Agenda, on_delete=models.CASCADE, null=False)
    paciente = models.ForeignKey(UsuarioCustomizado, on_delete=models.CASCADE, null=False)

