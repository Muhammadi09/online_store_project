from django.urls import path
from .views import ProductsByCategory

urlpatterns = [
    path('', ProductsByCategory.as_view(), name='productByCategory'),
]