from rest_framework.serializers import ModelSerializer

from medicar.agenda.models import Agenda


class ListAgendaSerializer(ModelSerializer):
    class Meta:
        model = Agenda
        fields = ('id', 'medico', 'dia', 'horarios')
        depth = 2
