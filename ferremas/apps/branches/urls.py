from django.urls import path
from .api import BranchListView, AddBranchView, BranchDetailView

urlpatterns = [
    path('branches/', BranchListView.as_view(), name='branch-list'),
    path('branches/add/', AddBranchView.as_view(), name='add-branch'),
    path('branches/<int:pk>/', BranchDetailView.as_view(), name='branch-detail'),
]
