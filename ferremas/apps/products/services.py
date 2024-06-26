from .models import Product
from apps.prices.models import Prices
from django.db.models import OuterRef, Subquery

def get_active_products():
    product = Product.objects.filter(is_active=True)
    return product


def create_product(name, description, price):
    # Verifica si ya existe un producto con el mismo nombre
    if Product.objects.filter(name=name).exists():
        return False, "A product with the same name already exists"
    else:
        # Crea un nuevo producto
        product = Product(name=name, description=description)
        product.save()
        return True, "Product created successfully"


def get_products_with_latest_prices():
    latest_price_subquery = Prices.objects.filter(
        id_product=OuterRef('id')
    ).order_by('-created_at').values('price')[:1]

    products_with_prices = Product.objects.annotate(
        latest_price=Subquery(latest_price_subquery)
    )
    
    return products_with_prices