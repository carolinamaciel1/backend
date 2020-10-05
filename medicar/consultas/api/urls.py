from django.urls import path

from medicar.consultas.api.views import ListConsultasView

app_name = "consultas"
urlpatterns = [
    path("", view=ListConsultasView.as_view(), name="list_consultas"),
]
