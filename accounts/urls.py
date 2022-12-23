from django.urls import path
from .views import customer_signup



urlpatterns = [
    path('signup/', customer_signup, name='signup'),
    
]
