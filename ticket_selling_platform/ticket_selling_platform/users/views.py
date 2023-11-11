from rest_framework import generics, permissions
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView
from .models import User
from .serializers import UserSerializer


class UserRegistrationView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]


class UserLoginView(TokenObtainPairView):
    pass


class TokenRefresh(TokenRefreshView):
    pass
