from django.urls import path, include
from .views import CreateUserView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
        path('register/', CreateUserView.as_view(), name="register"),
        path('login/', TokenObtainPairView.as_view(), name="token_obtain_pair"),
        path('refresh/', TokenRefreshView.as_view(), name="token_refresh"),
        path('api-auth/', include("rest_framework.urls")),
    ]
