from django.urls import path
from medicar.medicos.api.views import ListMedicosView

app_name = "medicos"
urlpatterns = [
    path("", view=ListMedicosView.as_view(), name="list_medicos"),
]
