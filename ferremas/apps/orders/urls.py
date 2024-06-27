from django.urls import path
from .api import OrderListView, UserOrderListView, FinalizeOrderView

urlpatterns = [
    path('orders/finalize/', FinalizeOrderView.as_view(), name='finalize-order'),
    path('orders/', OrderListView.as_view(), name='order-list'),
    path('orders/<str:username>/', UserOrderListView.as_view(), name='user-order-list'),
    
]
