from rest_framework.serializers import ModelSerializer
from medicar.especialidades.models import Especialidade


class ListEspecialidadesSerializer(ModelSerializer):

    class Meta:
        model = Especialidade
        fields = ('id', 'nome')
