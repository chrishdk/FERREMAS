from django.urls import path
from .api import CategoryListView, CategoryCreateView

urlpatterns = [
    path('categories/', CategoryListView.as_view(), name='category-list'),
    path('categories/create/', CategoryCreateView.as_view(), name='category-create'),


    
]
