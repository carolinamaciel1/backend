from django.urls import path

from medicar.users.api.views import RegistrationUserView

app_name = "users"
urlpatterns = [
    path("register/", view=RegistrationUserView.as_view(), name="register_user"),
]
