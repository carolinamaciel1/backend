from rest_framework.generics import ListAPIView
from medicar.especialidades.api.serializers import ListEspecialidadesSerializer
from medicar.especialidades.models import Especialidade
from rest_framework import filters


class ListEspecialidadesView(ListAPIView):
    serializer_class = ListEspecialidadesSerializer
    queryset = Especialidade.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['nome']
