import pytest
from apps.products.models import Product

@pytest.mark.django_db
class TestProductModels:
    def test_product_creation(self):
        product = Product.objects.create(name="Test Product", description="Test Description", is_active=True)
        assert product.name == "Test Product"
        assert product.description == "Test Description"
        assert product.is_active is True

    def test_product_str_method(self):
        product = Product.objects.create(name="Test Product", description="Test Description")
        assert str(product) == "Test Product"

    def test_product_deactivate_method(self):
        product = Product.objects.create(name="Test Product", description="Test Description", is_active=True)
        product.deactivate()
        assert product.is_active is False

    def test_product_update(self):
        product = Product.objects.create(name="Test Product", description="Test Description", is_active=True)
        product.name = "Updated Product"
        product.save()
        updated_product = Product.objects.get(id=product.id)
        assert updated_product.name == "Updated Product"

    def test_product_creation_deactivate(self):
        product = Product.objects.create(name="Test Product", description="Test Description", is_active=False)
        assert product.name == "Test Product"
        assert product.description == "Test Description"
        assert product.is_active is False
