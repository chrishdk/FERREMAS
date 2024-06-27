import pytest
from apps.products.models import Product
from apps.prices.models import Prices
from apps.products.services import get_active_products, create_product, get_products_with_latest_prices

@pytest.mark.django_db
class TestProductService:
    def setup_method(self):
        # Configuración de datos de prueba
        self.product1 = Product.objects.create(name="Test Product 1", description="Description 1", is_active=True)
        self.product2 = Product.objects.create(name="Test Product 2", description="Description 2", is_active=False)
        self.price1 = Prices.objects.create(id_product=self.product1, price=100, created_at="2023-01-01")
        self.price2 = Prices.objects.create(id_product=self.product1, price=150, created_at="2023-02-01")

    def test_get_active_products(self):
        """
        Validar que la función get_active_products devuelva solo los productos activos.
        """
        active_products = get_active_products()
        assert self.product1 in active_products
        assert self.product2 not in active_products

    def test_create_product(self):
        """
        Validar que la función create_product cree un nuevo producto correctamente y no permita duplicados.
        """
        success, message = create_product("New Product", "New Description", 200)
        assert success is True
        assert message == "Product created successfully"
        assert Product.objects.filter(name="New Product").exists()

        # Probar la creación de un producto con el mismo nombre
        success, message = create_product("Test Product 1", "New Description", 200)
        assert success is False
        assert message == "A product with the same name already exists"

    def test_get_products_with_latest_prices(self):
        """
        Validar que la función get_products_with_latest_prices devuelva productos con el precio más reciente.
        """
        products_with_prices = get_products_with_latest_prices()
        product_with_price = products_with_prices.get(id=self.product1.id)
        assert product_with_price.latest_price == 150
