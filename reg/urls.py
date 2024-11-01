from django.urls import path
from .views import UserRegisterView, UserLoginView, CustomTokenObtainPairView

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='user-register'),
    path('login/', UserLoginView.as_view(), name='user-login'),
    path('token/', CustomTokenObtainPairView.as_view(), name='token-obtain-pair'),
]
