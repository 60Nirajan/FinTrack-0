from django.urls import path
from rest_framework_simplejwt import views as jwt_views

from . views import UserRegistrationView, UserLoginView

urlpatterns = [
    path('auth/users/', UserRegistrationView.as_view()),
    path('auth/jwt/create/', UserLoginView.as_view()),
    path('auth/jwt/refresh/', jwt_views.TokenRefreshView.as_view()),
]
