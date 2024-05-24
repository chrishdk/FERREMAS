from stock.models import Stock
from .models import Cart, CartItem

def check_stock(product_id, branch_id, quantity):
    try:
        stock = Stock.objects.get(product_id=product_id, branch_id=branch_id)
        if stock.quantity >= quantity:
            return True, "Sufficient stock available"
        else:
            return False, "Insufficient stock available"
    except Stock.DoesNotExist:
        return False, "Stock information not available"

def add_to_cart(cart, product_id, branch_id, quantity):
    success, message = check_stock(product_id, branch_id, quantity)
    if success:
        # Add item to cart
        cart_item, created = CartItem.objects.get_or_create(
            product_id=product_id, branch_id=branch_id, defaults={'quantity': quantity})
        if not created:
            cart_item.quantity += quantity
            cart_item.save()
        cart.items.add(cart_item)
        cart.save()
        return True, "Product added to cart"
    else:
        return False, message


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
