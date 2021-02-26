from django.shortcuts import render, get_object_or_404
from .models import Customer
from django.views import generic


class CustomersIndexView(generic.ListView):
    context_object_name = 'customers'
    template_name = 'customers/index.html'
    
    def get_queryset(self):
        return Customer.objects.all()
    
    
class CustomersDetailView(generic.DetailView):
    model = Customer
    template_name = 'customers/detail.html' 