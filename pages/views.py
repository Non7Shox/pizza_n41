from django.shortcuts import render
from django.views.generic import TemplateView

from pages.models import ScrollModel
from products.models import ProductModel


class HomePageView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        pizza = ProductModel.objects.filter(category__name='Pizza')
        burgers = ProductModel.objects.filter(category__name='Burgers')
        salad = ProductModel.objects.filter(category__name='Salad')
        fries = ProductModel.objects.filter(category__name='Fries')
        drinks = ProductModel.objects.filter(category__name='Drinks')
        discount_products = ScrollModel.objects.all()[:5]
        context = {
            'pizza': pizza,
            'burgers': burgers,
            'salad': salad,
            'fries': fries,
            'drinks': drinks,
            'discount_products': discount_products
        }
        return context
