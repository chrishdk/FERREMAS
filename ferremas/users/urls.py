from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name='productos-list-create'),
    path('register/', views.register, name='productos-detail'),
    path('profile/' ,views.profile, name='producto-detalle'),
    ]