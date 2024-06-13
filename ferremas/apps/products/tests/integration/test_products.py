import pytest
from rest_framework.test import APIClient
from django.urls import reverse
from rest_framework import status

@pytest.mark.django_db
class TestAccountAPI:
    def test_create_producto(self):

        client = APIClient()

        url = reverse('add-to-product')

        data = {
            'name': 'Producto1',
            'description': 'Producto1',
            'price': '79990'
        }

        response = client.post(url, data, format='json')

        assert response.status_code == status.HTTP_201_CREATED

    def test_create_producto_no_name(self):

        client = APIClient()

        url = reverse('add-to-product')

        data = {
            'name': '',
            'description': 'taladrito',
            'price': '111'
        }

        response = client.post(url, data, format='json')

        assert response.status_code == status.HTTP_400_BAD_REQUEST


    def test_create_producto_no_price(self):

        client = APIClient()

        url = reverse('add-to-product')

        data = {
            'name': 'Producto1',
            'description': 'taladrito',
            'price': ''
        }

        response = client.post(url, data, format='json')

        assert response.status_code == status.HTTP_400_BAD_REQUEST

    def test_create_producto_price_especial(self):

        client = APIClient()

        url = reverse('add-to-product')

        data = {
            'name': 'Producto1',
            'description': 'taladrito',
            'price': '79.999#'
        }

        response = client.post(url, data, format='json')

        assert response.status_code == status.HTTP_400_BAD_REQUEST