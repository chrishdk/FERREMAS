from django.urls import path
from .api import ProductListView, AddProductView, ProductActiveListView, ProductDeactivateView, ProductActivateView

urlpatterns = [
    path('products/', ProductListView.as_view(), name='product-list'),
    path('products/add/', AddProductView.as_view(), name='add-to-product'),
    path('products/all/', ProductActiveListView.as_view(), name='all-products'),
    path('products/deactivate/', ProductDeactivateView.as_view(), name='deactivate-product'),
    path('products/activate/', ProductActivateView.as_view(), name='activate-product')
]