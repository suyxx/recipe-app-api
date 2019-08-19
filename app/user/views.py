from rest_framework import generics
from user.serializers import UserSerializer,AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework import generics, authentication, permissions

# Create your views here.

class CreateUserView(generics.CreateAPIView):
    serializer_class = UserSerializer

class CreateTokenView(ObtainAuthToken):

    serializer_class = AuthTokenSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES

class ManageUserView(generics.RetrieveUpdateAPIView):

    serializer_class = UserSerializer
    authentication_classes = (authentication, permissions.IsAuthenticated,)

    def get_object(self):
        return self.request.user
