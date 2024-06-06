import pytest
from rest_framework.test import APIClient
from django.urls import reverse
from rest_framework import status

@pytest.mark.django_db
class TestAccountAPI:
    def test_user_products_successfully(self):
        """
        Test para verificar que el endpoint de registro de productos funciona correctamente.
        """
        client = APIClient()

        url = reverse('add-to-product')

        data = {
            'name': '',
            'description': 'taladrito',
            'price': '111'
        }

        response = client.post(url, data, format='json')

        assert response.status_code == status.HTTP_201_CREATED

        # assert 'name' in response.data

        # assert response.data['name'] == 'taladro'