from rest_framework import generics, permissions
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
from .serializers import RegisterSerializer, LoginSerializer
from rest_framework.views import APIView
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authentication import TokenAuthentication

User = get_user_model()

class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]

class LoginView(ObtainAuthToken):
    permission_classes = [permissions.AllowAny]

class ProfileView(APIView):
    authentication_classes = [TokenAuthentication]  # <-- Required!
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        user = request.user
        token, _ = Token.objects.get_or_create(user=user)
        return Response({
            "username": user.username,
            "email": user.email,
            "bio": getattr(user, "bio", ""),
            "token": token.key
        })
