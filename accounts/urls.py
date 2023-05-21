from django.urls import path
from .views import customer_signup, ProfileView, ProfileEditView, AddAddressView, updateAddressView, confirm_delete_address



urlpatterns = [
    path('signup/', customer_signup, name='signup'),
    path('profile/<int:pk>/', ProfileView, name='profile'),
    path('profile/<int:pk>/edit', ProfileEditView, name='profile_edit'),
    path('profile/<int:pk>/add_address', AddAddressView, name='add_address'),
    path('profile/<int:customer_pk>/address/<int:address_id>/update/', updateAddressView, name='update_address'),
    path('profile/<int:customer_pk>/address/<int:address_id>/confirm_delete/', confirm_delete_address, name='confirm_delete_address'),
    
]
