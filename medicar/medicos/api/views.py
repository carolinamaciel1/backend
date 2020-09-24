from rest_framework.generics import ListAPIView
from medicar.medicos.api.serializers import ListMedicosSerializer
from medicar.medicos.models import Medico
from rest_framework import filters


class ListMedicosView(ListAPIView):
    serializer_class = ListMedicosSerializer
    queryset = Medico.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['nome', 'especialidade__id']
