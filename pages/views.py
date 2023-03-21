from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from products.models import Category, Product


class HomePageView(ListView):
    model = Product
    template_name = 'home.html'

class BasePageView(ListView):
    model = Category
    template_name = 'base.html'


