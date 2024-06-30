import pytest
from django.test import TestCase
from datetime import datetime
from rest_framework.test import APIClient
from django.urls import reverse
from apps.products.models import Product
from apps.branches.models import Branch
from apps.stock.models import Stock
from apps.carts.models import Cart, CartItem
from apps.prices.models import Prices
from apps.carts.services import add_to_cart, check_stock


@pytest.mark.django_db
def test_cart_model():
    # Crear una instancia de Cart
    cart = Cart.objects.create(user="testuser")

    # Verificar el método __str__()
    assert str(cart) == "Carrito de testuser"

    # Verificar que los campos se hayan guardado correctamente
    assert cart.user == "testuser"
    assert isinstance(cart.created_at, datetime)
    assert isinstance(cart.updated_at, datetime)
    assert cart.created_at <= cart.updated_at


@pytest.mark.django_db
def test_cart_item_model():
    # Crear instancias relacionadas necesarias
    cart = Cart.objects.create(user="testuser")
    product = Product.objects.create(name="Test Product", description="Description", is_active=True)

    # Crear una instancia de CartItem
    cart_item = CartItem.objects.create(
        cart=cart,
        product=product,
        branch_id=1,
        quantity=5,
        price=10
    )

    # Verificar el método __str__()
    expected_str = f"5 x Test Product en Carrito de testuser"
    assert str(cart_item) == expected_str

    # Verificar que los campos se hayan guardado correctamente
    assert cart_item.cart == cart
    assert cart_item.product == product
    assert cart_item.branch_id == 1
    assert cart_item.quantity == 5
    assert cart_item.price == 10

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

@pytest.fixture
def price(product):
    return Prices.objects.create(id_product=product, price=10)

@pytest.mark.django_db
def test_add_to_cart(api_client, product, branch, stock, price):
    user = "testuser"
    product_id = product.id
    branch_id = branch.id
    quantity = 3

    success, message = add_to_cart(user, product_id, branch_id, quantity)
    assert success is True
    assert message == "Product added to cart successfully."

    # Verificar que el carrito tenga el ítem agregado correctamente
    cart = Cart.objects.get(user=user)
    cart_item = CartItem.objects.get(cart=cart, product=product, branch_id=branch_id)
    assert cart_item.quantity == quantity
    assert cart_item.price == price.price

@pytest.mark.django_db
def test_check_stock_with_sufficient_quantity(product, branch, stock):
    product_id = product.id
    branch_id = branch.id
    quantity = 50

    success, message = check_stock(product_id, branch_id, quantity)
    assert success is True
    assert message == f"Sufficient stock available for {product.name}"

@pytest.mark.django_db
def test_check_stock_with_insufficient_quantity(product, branch, stock):
    product_id = product.id
    branch_id = branch.id
    quantity = 150

    success, message = check_stock(product_id, branch_id, quantity)
    assert success is False
    assert message == f"Insufficient stock available for {product.name}"

@pytest.mark.django_db
def test_check_stock_with_inactive_product(product, branch, stock):
    product.is_active = False
    product.save()

    product_id = product.id
    branch_id = branch.id
    quantity = 50

    success, message = check_stock(product_id, branch_id, quantity)
    assert success is False
    assert message == "Stock information not available"