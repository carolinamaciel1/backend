from django.urls import path
from medicar.agenda.api.views import ListAgendaView

app_name = "agenda"
urlpatterns = [
    path("", view=ListAgendaView.as_view(), name="list_agenda"),
]
