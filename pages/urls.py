from django.urls import path
from .views import BasePageView, HomePageView

urlpatterns = [
    path('home/', HomePageView.as_view(), name='home'),
    path('', BasePageView.as_view(), name='base'),
]
