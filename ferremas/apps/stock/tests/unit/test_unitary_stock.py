import pytest
from rest_framework.test import APIRequestFactory
from apps.stock.api import TotalStockView, AddStockToBranchView
from apps.products.models import Product
from apps.branches.models import Branch
from apps.stock.models import Stock
from django.db import IntegrityError

@pytest.fixture
def api_factory():
    return APIRequestFactory()

@pytest.fixture
def product():
    return Product.objects.create(name="Producto 1")

@pytest.fixture
def branch():
    return Branch.objects.create(nombre="Sucursal 1")

@pytest.fixture
def stock(product, branch):
    return Stock.objects.create(product=product, branch=branch, quantity=100)

# Pruebas para api.py

@pytest.mark.django_db
#Verifica que la vista TotalStockView devuelve el stock total 
def test_total_stock_view(api_factory, stock):
    view = TotalStockView.as_view()
    request = api_factory.get('/stock/total/')
    response = view(request)
    assert response.status_code == 200
    assert len(response.data) == 1
    assert response.data[0]['quantity'] == 100


# Pruebas para models.py

@pytest.mark.django_db
#Verifica que se puede crear un registro de Stock y que sus campos se guardan correctamente
def test_create_stock(product, branch):
    stock = Stock.objects.create(product=product, branch=branch, quantity=100)
    assert stock.quantity == 100
    assert stock.product == product
    assert stock.branch == branch


@pytest.mark.django_db
#Verifica que la restricción de unicidad en el modelo Stock se cumple, es decir, 
# no se pueden crear dos registros de Stock con la misma combinación de product y branch.
def test_unique_constraint(product, branch):
    Stock.objects.create(product=product, branch=branch, quantity=100)
    with pytest.raises(IntegrityError):
        Stock.objects.create(product=product, branch=branch, quantity=50)


