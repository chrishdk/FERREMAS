from django.urls import path
from .api import ActiveProductListView, AddProductView

urlpatterns = [
    path('products/', ActiveProductListView.as_view(), name='product-list'),
    path('products/add/', AddProductView.as_view(), name='add-to-product'),
]