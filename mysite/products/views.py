from django.shortcuts import render, get_object_or_404
from .models import Product
from django.views import generic


class ProductsIndexView(generic.ListView):
    context_object_name = 'products'
    template_name = 'products/index.html'

    def get_queryset(self):
        return Product.objects.all()


class ProductsDetailView(generic.DetailView):
    model = Product
    template_name = 'products/detail.html'