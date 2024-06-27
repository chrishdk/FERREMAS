# orders/services.py

from decimal import Decimal
from django.db import transaction
from .models import Order, OrderItem
from apps.stock.models import Stock
from apps.carts.models import Cart, CartItem
from apps.branches.models import Branch

def finalize_order(user):
    try:
        cart = Cart.objects.get(user=user)
        if cart.items.exists():
            total_amount = Decimal('0.00')
            
            with transaction.atomic():
                order = Order.objects.create(total_amount=total_amount, is_paid=True, user=user)
                
                for item in cart.items.all():
                    stock = Stock.objects.get(product=item.product, branch_id=item.branch_id, product__is_active=True)
                    if stock.quantity < item.quantity:
                        raise ValueError("Insufficient stock for product: {}".format(item.product.name))
                    
                    stock.quantity -= item.quantity
                    stock.save()
                    
                    branch = Branch.objects.get(id=item.branch_id)
                    
                    OrderItem.objects.create(
                        order=order,
                        product_name=item.product.name,
                        product_description=item.product.description,
                        branch_name=branch.nombre,
                        quantity=item.quantity,
                        price=item.price
                    )
                    total_amount += item.price * item.quantity

                order.total_amount = total_amount
                order.save()
                
                cart.items.all().delete()  # Elimina los elementos del carrito

            return order
        else:
            raise ValueError("El carrito está vacío. No se puede crear una orden con monto 0.")

    except Cart.DoesNotExist:
        raise ValueError("Cart not found")
    except Stock.DoesNotExist:
        raise ValueError("Stock information not available for some products")
    except Branch.DoesNotExist:
        raise ValueError("Branch not found")
