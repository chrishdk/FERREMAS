from .models import CartItem, Cart
from apps.products.models import Product
from apps.stock.models import Stock
from apps.prices.models import Prices


def remove_from_cart(cart, product_id, branch_id, quantity):
    try:
        cart_item = CartItem.objects.get(product_id=product_id, branch_id=branch_id, cart=cart)
        if cart_item.quantity <= quantity:
            cart.items.remove(cart_item)
            cart_item.delete()
            return True, "Product removed from cart"
        else:
            cart_item.quantity -= quantity
            cart_item.save()
            return True, "Product quantity updated in cart"
    except CartItem.DoesNotExist:
        return False, "Product not found in cart"


def check_stock(product_id, branch_id, quantity):
    try:
        stock = Stock.objects.get(product_id=product_id, branch_id=branch_id, product__is_active=True)
        product = stock.product
        if stock.quantity >= quantity:
            return True, f"Sufficient stock available for {product.name}"
        else:
            return False, f"Insufficient stock available for {product.name}"
    except Stock.DoesNotExist:
        return False, "Stock information not available"

def add_to_cart(user, product_id, branch_id, quantity):
    success, message = check_stock(product_id, branch_id, quantity)
    if not success:
        return False, message

    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist:
        return False, "Product does not exist."

    # Get or create a cart for the user
    cart, created = Cart.objects.get_or_create(user=user)

    # Get the latest price
    price_record = Prices.objects.filter(id_product=product_id).order_by('-created_at').first()
    if not price_record:
        return False, "Price not available for the product."

    cart_item, created = CartItem.objects.get_or_create(
        cart=cart,
        product=product,
        branch_id=branch_id,
        defaults={'quantity': quantity, 'price': price_record.price}
    )

    if not created:
        cart_item.quantity += quantity
        cart_item.save()

    return True, "Product added to cart successfully."