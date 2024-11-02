from django.contrib.auth.models import User  # Import User model
from django.shortcuts import render
from rest_framework import viewsets, filters, status
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from django_filters.rest_framework import DjangoFilterBackend
from .models import Employee
from .serializers import EmployeeSerializer, RegisterSerializer  # Ensure you have this serializer

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        # Add custom claims here if needed
        return token

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

    def post(self, request, *args, **kwargs):
        # Directly use the parent method without checking for the user
        return super().post(request, *args, **kwargs)

class RegisterView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            tokens = serializer.get_tokens_for_user(user)
            return Response(tokens, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all().order_by('id')
    serializer_class = EmployeeSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filterset_fields = ['department', 'role']
    search_fields = ['department', 'role'] 
    ordering_fields = ['date_joined', 'name'] 

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)
