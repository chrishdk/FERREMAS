from django.urls import path
from .api import AddToCartView, RemoveFromCartView, GetCartUserView

urlpatterns = [
    # URL para agregar productos al carrito
    path('cart/user/', GetCartUserView.as_view(), name='get-cart-user'),
    path('cart/add/', AddToCartView.as_view(), name='add-to-cart'),
    path('cart/remove/', RemoveFromCartView.as_view(), name='remove-from-cart'),
]
