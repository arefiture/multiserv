from django.urls import path
from users.views import RegisterView, CustomTokenObtainPairView, UserDetailView

urlpatterns = [
    path('api/auth/register/', RegisterView.as_view()),
    path('api/auth/login/', CustomTokenObtainPairView.as_view()),
    # path('api/auth/user/', UserDetailView.as_view()),
]