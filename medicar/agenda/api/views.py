from rest_framework import filters
from rest_framework.generics import ListAPIView

from medicar.agenda.api.serializers import ListAgendaSerializer
from medicar.agenda.models import Agenda


class ListAgendaView(ListAPIView):
    serializer_class = ListAgendaSerializer
    queryset = Agenda.objects.all().order_by('dia')
    filter_backends = [filters.SearchFilter]
    # search_fields = ['medico__id']