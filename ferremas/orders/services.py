from decimal import Decimal
from django.db import transaction
from .models import Order, OrderItem
from stock.models import Stock
from carts.models import Cart, CartItem

def finalize_order(cart_id):
    try:
        cart = Cart.objects.get(id=cart_id)
        total_amount = Decimal('0.00')
        
        with transaction.atomic():
            order = Order.objects.create(total_amount=total_amount, is_paid=True)
            
            for item in cart.items.all():
                stock = Stock.objects.get(product=item.product, branch=item.branch, product__is_active = True)
                if stock.quantity < item.quantity:
                    raise ValueError("Insufficient stock for product: {}".format(item.product.name))
                
                stock.quantity -= item.quantity
                stock.save()
                
                order_item = OrderItem.objects.create(
                    order=order,
                    product=item.product,
                    branch=item.branch,
                    quantity=item.quantity,
                    price=item.product.price
                )
                total_amount += item.product.price * item.quantity

            order.total_amount = total_amount
            order.save()
            
            cart.items.clear() 

        return order

    except Cart.DoesNotExist:
        raise ValueError("Cart not found")
    except Stock.DoesNotExist:
        raise ValueError("Stock information not available for some products")
