from django.urls import path
from .api import ActiveProductListView, AddProductView, ProductWithLatestPriceListView

urlpatterns = [
    path('products/', ActiveProductListView.as_view(), name='product-list'),
    path('products/add/', AddProductView.as_view(), name='add-to-product'),
    path('products/all/', ProductWithLatestPriceListView.as_view(), name='all-products')
]