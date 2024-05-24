from django.urls import path
from .api import TotalStockView, BranchStockView, AddStockToBranchView

urlpatterns = [
    path('stock/total/', TotalStockView.as_view(), name='total-stock'),
    path('stock/branch/<int:branch_id>/', BranchStockView.as_view(), name='branch-stock'),
    path('stock/branch/add/', AddStockToBranchView.as_view(), name='add-stock-to-branch'),
]
