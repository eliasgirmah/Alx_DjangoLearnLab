# accounts/views.py
from rest_framework import generics, status
from rest_framework.response import Response
from .serializers import RegisterSerializer, UserSerializer
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.views import ObtainAuthToken

User = get_user_model()

class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        # create token
        token, _ = Token.objects.get_or_create(user=user)
        data = UserSerializer(user).data
        data['token'] = token.key
        return Response(data, status=status.HTTP_201_CREATED)

# You can use DRF's built-in ObtainAuthToken for login
class LoginView(ObtainAuthToken):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        # returns {"token": "..."}
        response = super().post(request, *args, **kwargs)
        token = Token.objects.get(key=response.data['token'])
        user = token.user
        user_data = UserSerializer(user).data
        user_data['token'] = token.key
        return Response(user_data)
