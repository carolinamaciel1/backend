from rest_framework import filters
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from medicar.consultas.api.serializers import ListConsultasSerializer
from medicar.consultas.models import Consulta


class ListConsultasView(ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = ListConsultasSerializer
    queryset = Consulta.objects.all().order_by('agenda__dia')
    filter_backends = [filters.SearchFilter]

