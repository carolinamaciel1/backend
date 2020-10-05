from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny

from medicar.users.api.serializers import UserRegistrationSerializer


class RegistrationUserView(CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = UserRegistrationSerializer
