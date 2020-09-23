from django.db import models
from django.utils.translation import ugettext_lazy as _


class Especialidade(models.Model):
    def __str__(self):
        return self.nome

    # add unique=True?
    nome = models.CharField(max_length=200, verbose_name=_('Especialidade'), unique=True, blank=False, null=False)
