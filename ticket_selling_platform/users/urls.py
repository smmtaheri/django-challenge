from django.urls import path
from .views import UserRegistrationView, UserLoginView, TokenRefresh

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('token/refresh/', TokenRefresh.as_view(), name='token_refresh'),
]
