from django.shortcuts import render
from django.views import generic
from .models import Order

class OrdersIndexView(generic.ListView):
    context_object_name = 'orders'
    template_name = 'orders/index.html'

    def get_queryset(self):
        return Order.objects.all()

class OrdersDetailView(generic.DetailView):
    model = Order
    template_name = 'orders/detail.html'