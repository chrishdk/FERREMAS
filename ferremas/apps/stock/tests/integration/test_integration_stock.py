import pytest
from rest_framework.test import APIClient
from django.urls import reverse
from rest_framework import status
from apps.products.models import Product
from apps.branches.models import Branch
from apps.stock.models import Stock

@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def product():
    return Product.objects.create(name="Producto 1")

@pytest.fixture
def branch():
    return Branch.objects.create(nombre="Sucursal 1")

@pytest.fixture
def stock(product, branch):
    return Stock.objects.create(product=product, branch=branch, quantity=100)

@pytest.mark.django_db
#Prueba para obtener el stock total de todos los productos en todas las sucursales

def test_total_stock_view(api_client, stock):
    url = reverse('total-stock')
    response = api_client.get(url)
    assert response.status_code == 200
    assert len(response.data) == 1
    assert response.data[0]['quantity'] == 100

@pytest.mark.django_db
#Prueba para obtener el stock de una sucursal específica.

def test_branch_stock_view(api_client, branch, stock):
    url = reverse('branch-stock', args=[branch.id])
    response = api_client.get(url)
    assert response.status_code == 200
    assert len(response.data) == 1
    assert response.data[0]['branch'] == branch.id

#Prueba para añadir stock a una sucursal existente.

@pytest.mark.django_db
def test_add_stock_to_existing_branch(api_client, product, branch, stock):
    url = reverse('add-stock-to-branch')
    data = {
        'product': product.id,
        'branch': branch.id,
        'quantity': 50
    }
    response = api_client.post(url, data, format='json')
    assert response.status_code == 200
    stock.refresh_from_db()
    assert stock.quantity == 150