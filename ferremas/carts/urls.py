from django.urls import path
from .api import AddToCartView, RemoveFromCartView, GetCartView

urlpatterns = [
    # URL para agregar productos al carrito
    path('cart/<int:cart_id>/', GetCartView.as_view(), name='get-cart'),
    path('cart/add/', AddToCartView.as_view(), name='add-to-cart'),
    path('cart/remove/', RemoveFromCartView.as_view(), name='remove-from-cart'),
]
