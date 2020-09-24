from rest_framework.serializers import ModelSerializer
from medicar.medicos.models import Medico


class ListMedicosSerializer(ModelSerializer):
    class Meta:
        model = Medico
        fields = ('id', 'crm', 'nome', 'especialidade')
        depth = 1

