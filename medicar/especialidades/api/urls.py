from django.urls import path
from medicar.especialidades.api.views import ListEspecialidadesView

app_name = "especialidades"
urlpatterns = [
    path("", view=ListEspecialidadesView.as_view(), name="list_especialidade"),
]
