from django.urls import path
from .api import FinalizeOrderView

urlpatterns = [
    path('orders/finalize/', FinalizeOrderView.as_view(), name='finalize-order'),
]
