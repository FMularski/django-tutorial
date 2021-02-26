from django.shortcuts import render, get_object_or_404
from .models import Customer, Order


def index(request):
    customers = Customer.objects.all()
    return render(request, 'customers/index.html', {'customers': customers})

def detail(request, customer_id):
    customer = get_object_or_404(Customer, pk=customer_id)
    return render(request, 'customers/detail.html', {'customer': customer})

def order(request, customer_id, order_id):
    order = get_object_or_404(Order, pk=order_id)
    return render(request, 'customers/order.html', {'order': order})