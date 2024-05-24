from django.urls import path
from .api import TotalStockView, BranchStockView, AddStockToBranchView

urlpatterns = [
    # URL para consultar el stock total de todos los productos en todas las sucursales
    path('stock/total/', TotalStockView.as_view(), name='total-stock'),

    # URL para consultar el stock por sucursal utilizando el ID de la sucursal
    path('stock/branch/<int:branch_id>/', BranchStockView.as_view(), name='branch-stock'),

    path('stock/branch/add/', AddStockToBranchView.as_view(), name='add-stock-to-branch'),
]
