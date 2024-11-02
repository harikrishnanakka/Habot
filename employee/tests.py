from django.test import TestCase

# Create your tests here.
# employee/tests.py
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from django.contrib.auth.models import User
from .models import Employee

class EmployeeTests(APITestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username='testuser', password='testpass')
        
        # Obtain a token for the test user
        url = reverse('token_obtain_pair')
        response = self.client.post(url, {'username': 'testuser', 'password': 'testpass'}, format='json')
        self.token = response.data['access']
        
        # Include the token in the headers
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')

    def test_create_employee(self):
        url = reverse('employee-list')
        data = {'name': 'John Doe', 'email': 'john@example.com'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_employees(self):
        url = reverse('employee-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

