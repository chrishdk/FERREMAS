from .models import Product

def get_active_products():
    # Retorna todos los productos activos
    return Product.objects.filter(is_active=True)

def create_product(name, description, price):
    # Verifica si ya existe un producto con el mismo nombre
    if Product.objects.filter(name=name).exists():
        return False, "A product with the same name already exists"
    else:
        # Crea un nuevo producto
        product = Product(name=name, description=description, price=price)
        product.save()
        return True, "Product created successfully"
