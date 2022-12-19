from django.urls import path
from .views import SignUpCustomer

urlpatterns = [
    path('signup/', SignUpCustomer, name='signup'),
]
