import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from apps.products.models import Product
from apps.prices.models import Prices
import time

@pytest.fixture
def api_client():
    return APIClient()

@pytest.mark.django_db(transaction=True)
class TestProductAPIViews:
    def test_get_active_products(self, api_client):
        # Crear productos para probar
        product1 = Product.objects.create(name="Product 1", description="Description 1", is_active=True)
        product2 = Product.objects.create(name="Product 2", description="Description 2", is_active=False)
        
        url = reverse('all-products')
        response = api_client.get(url)
        
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 1
    

    def test_create_product(self, api_client):
        url = reverse('add-to-product')
        data = {
            'name': 'New Product',
            'description': 'New Description',
            'price': 100,
        }
        response = api_client.post(url, data, format='json')
        
        assert response.status_code == status.HTTP_201_CREATED
        assert Product.objects.filter(name='New Product').exists()
    

    def test_get_products_with_latest_prices(self, api_client):
        # Crear productos y precios para probar
        product1 = Product.objects.create(name="Product 1", description="Description 1", is_active=True)
        product2 = Product.objects.create(name="Product 2", description="Description 2", is_active=True)
        
        # Añadir precios a los productos
        Prices.objects.create(id_product=product1, price=100)
        time.sleep(2)
        Prices.objects.create(id_product=product1, price=150)
        time.sleep(2)
        Prices.objects.create(id_product=product2, price=200)
        time.sleep(2)
        Prices.objects.create(id_product=product2, price=250)
        time.sleep(2)

        url = reverse('all-products')
        response = api_client.get(url)
        

        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 2

        assert response.data[0]['name'] == 'Product 1'
        assert int(response.data[0]['latest_price']) == 150
        assert response.data[1]['name'] == 'Product 2'
        assert int(response.data[1]['latest_price']) == 250


    def test_create_product_duplicate_name(self):
        client = APIClient()
        url = reverse('add-to-product')
        data = {
            'name': 'Test Product',
            'description': 'Product Description'
        }

        response_first = client.post(url, data, format='json')
        assert response_first.status_code == status.HTTP_201_CREATED
        assert response_first.data['message'] == "Product created successfully"

        response_second = client.post(url, data, format='json')
        assert response_second.status_code == status.HTTP_400_BAD_REQUEST
        assert response_second.data['message'] == "A product with the same name already exists"


    def test_product_deactivate(self):
        client = APIClient()
        url = reverse('add-to-product')
        data = {
            'name': 'Test Product',
            'description': 'Product Description'
        }

        response_first = client.post(url, data, format='json')
        assert response_first.status_code == status.HTTP_201_CREATED
        assert response_first.data['message'] == "Product created successfully"

        url= reverse('deactivate-product')
        data = {
            'name': 'Test Product'
        }
        response_second = client.post(url, data, format='json')
        assert response_second.status_code == status.HTTP_200_OK
        