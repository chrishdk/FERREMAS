from django.urls import path
from .api import PersonaList

urlpatterns = [
#     path('signup/', SignUpView.as_view(), name='signup'),
#     path('login/', LoginView.as_view(), name='login'),
#     path('profile/', ProfileView.as_view(), name='profile'),
    path('personas/', PersonaList.as_view(), name='personas-list')
]