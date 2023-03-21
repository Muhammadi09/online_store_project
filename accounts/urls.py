from django.urls import path
from .views import customer_signup, ProfileView, ProfileEditView



urlpatterns = [
    path('signup/', customer_signup, name='signup'),
    path('profile/<int:pk>/', ProfileView, name='profile'),
    path('profile/<int:pk>/edit', ProfileEditView, name='profile_edit'),
    
]
