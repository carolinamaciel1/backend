from rest_framework.serializers import ModelSerializer

from medicar.consultas.models import Consulta


class ListConsultasSerializer(ModelSerializer):
    class Meta:
        model = Consulta
        fields = ('id', 'horario', 'data_agendamento')
        depth = 2


