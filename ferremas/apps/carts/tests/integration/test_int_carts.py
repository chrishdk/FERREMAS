import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from apps.carts.models import Cart, CartItem
from apps.branches.models import Branch
from apps.products.models import Product
from apps.stock.models import Stock
from apps.prices.models import Prices



@pytest.mark.django_db
def test_get_cart_user():
    client = APIClient()
    cart = Cart.objects.create(user="testuser")

    url = reverse('get-cart-user')
    response = client.post(url, {"user": "testuser"}, format='json')

    assert response.status_code == 200
    assert response.data['user'] == 'testuser'

@pytest.mark.django_db
def test_get_cart_user_not_found():
    client = APIClient()

    url = reverse('get-cart-user')
    response = client.post(url, {"user": "nonexistentuser"}, format='json')

    assert response.status_code == 404
    assert response.data['message'] == 'Cart not found'

@pytest.mark.django_db
def test_remove_from_cart():
    client = APIClient()
    cart = Cart.objects.create(user="testuser")
    branch = Branch.objects.create(nombre="Branch 1", direccion="Address 1", telefono="123456789")
    product = Product.objects.create(name="Product 1", description="Description 1", is_active=True)
    item = CartItem.objects.create(cart=cart, product=product, branch_id=branch.id, quantity=5, price=10)

    url = reverse('remove-from-cart')
    response = client.post(url, {"user": "testuser", "product_id": product.id, "branch_id": branch.id, "quantity": 3}, format='json')

    assert response.status_code == 200
    assert Cart.objects.get(user="testuser").items.get(product=product).quantity == 2

@pytest.mark.django_db
def test_remove_from_cart_not_found():
    client = APIClient()

    url = reverse('remove-from-cart')
    response = client.post(url, {"user": "nonexistentuser", "product_id": 1, "branch_id": 1, "quantity": 3}, format='json')

    assert response.status_code == 404
    assert response.data['message'] == 'Cart not found'




@pytest.mark.django_db
def test_add_to_cart():
    client = APIClient()
    branch = Branch.objects.create(nombre="Branch 1", direccion="Address 1", telefono="123456789")
    product = Product.objects.create(name="Product 1", description="Description 1", is_active=True)
    price = Prices.objects.create(id_product=product, price=10)
    stock = Stock.objects.create(product=product, branch_id=branch.id, quantity=10)
    

    url = reverse('add-to-cart')
    response = client.post(url, {"user": "testuser", "product_id": product.id, "branch_id": branch.id, "quantity": 3}, format='json')

    assert response.status_code == 200
    cart = Cart.objects.get(user="testuser")
    assert cart is not None
    cart_item = CartItem.objects.get(cart=cart, product=product, branch_id=branch.id)
    assert cart_item.quantity == 3
    updated_stock = Stock.objects.get(product=product, branch_id=branch.id)
    assert updated_stock.quantity == 10

@pytest.mark.django_db
def test_add_to_cart_invalid_data():
    client = APIClient()

    url = reverse('add-to-cart')
    response = client.post(url, {"user": "testuser", "product_id": 999, "branch_id": 999, "quantity": 3}, format='json')

    assert response.status_code == 400
    assert 'message' in response.data