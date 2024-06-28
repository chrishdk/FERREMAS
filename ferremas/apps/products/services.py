from .models import Product
from apps.prices.models import Prices
from django.db.models import OuterRef, Subquery

def get_products():
    latest_price_subquery = Prices.objects.filter(
        id_product=OuterRef('id')
    ).order_by('-created_at').values('price')[:1]

    products_with_prices = Product.objects.annotate(
        latest_price=Subquery(latest_price_subquery)
    )
    return products_with_prices

def get_product_active():
    return Product.objects.filter(is_active=True)


def create_product(name, description, price):
    if Product.objects.filter(name=name).exists():
        return False, "A product with the same name already exists"
    else:
        product = Product(name=name, description=description)
        product.save()
        return True, "Product created successfully"


def get_products_with_latest_prices():
    latest_price_subquery = Prices.objects.filter(
        id_product=OuterRef('id')
    ).order_by('-created_at').values('price')[:1]

    products_with_prices = Product.objects.filter(is_active=True).annotate(
        latest_price=Subquery(latest_price_subquery)
    )
    
    return products_with_prices

def product_deactivate(name):
    try:
        product = Product.objects.get(name=name)
        if product.is_active is False:
            return False, "Product is already deactivated"
        else:
            product.deactivate()
            return True, "Product deactivated successfully"
    except Product.DoesNotExist:
        return False, "Product not found"
    

def product_activate(name):
    try:
        product = Product.objects.get(name=name)
        if product.is_active is True:
            return False, "Product is already activated"
        else:
            product.activate()
            return True, "Product activated successfully"
    except Product.DoesNotExist:
        return False, "Product not found"

