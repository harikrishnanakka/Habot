# employee/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EmployeeViewSet, RegisterView, CustomTokenObtainPairView
from rest_framework_simplejwt.views import TokenRefreshView

router = DefaultRouter()
router.register(r'employees', EmployeeViewSet)

urlpatterns = [
    path('', include(router.urls)),  # Register employee routes (CRUD endpoints)
    path('register/', RegisterView.as_view(), name='register'),  # User registration endpoint
    path('token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),  # Token obtain endpoint
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # Token refresh endpoint
]
