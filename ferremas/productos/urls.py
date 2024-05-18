from django.urls import path
from . import views

urlpatterns = [
    path('productos/', views.get_items, name='productos-list-create'),
    path('productos/<int:cod_producto>/', views.get_producto_detalle, name='productos-detail'),
    path('productos/registro/' ,views.registrar_producto, name='producto-detalle'),
    ]