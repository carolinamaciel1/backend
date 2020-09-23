from django.db import models
from django.utils.translation import ugettext_lazy as _
from medicar.especialidades.models import Especialidade
from medicar.medicos.medicos_utils import TELEFONE_MAX_LENGTH


class Medico(models.Model):

    def __str__(self):
        return self.nome

    nome = models.CharField(max_length=200, verbose_name=_('Nome'), blank=False, null=False)
    crm = models.CharField(max_length=13, verbose_name=_('CRM'), blank=False, null=False)
    email = models.CharField(max_length=200, verbose_name=_('Email'), blank=True, null=True)
    telefone = models.CharField(max_length=TELEFONE_MAX_LENGTH, verbose_name=_('Telefone'), blank=True, null=True)
    especialidade = models.ForeignKey(Especialidade, max_length=100, on_delete=models.CASCADE, blank=True, null=True)
