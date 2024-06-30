from .models import Stock

def update_stock(product, branch, quantity):
    # Verifica si ya existe un registro de stock para este producto y sucursal
    try:
        stock = Stock.objects.get(product=product, branch=branch)
        # Actualiza la cantidad en el stock existente
        stock.quantity += quantity
        stock.save()
    except Stock.DoesNotExist:
        # Crea un nuevo registro de stock si no existe uno
        stock = Stock(product=product, branch=branch, quantity=quantity)
        stock.save()



def add_stock(stock, quantity):
    stock.quantity += int(quantity)
    stock.save()
    return True, "Stock updated successfully"     




# def check_stock(product, branch, quantity):
#     # Verifica si hay suficiente stock disponible para el producto en la sucursal
#     try:
#         stock = Stock.objects.get(product=product, branch=branch)
#         if stock.quantity >= quantity:
#             return True, "Sufficient stock available"
#         else:
#             return False, "Insufficient stock available"
#     except Stock.DoesNotExist:
#         return False, "Stock information not available"
