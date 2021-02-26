from django.urls import path
from . import views

app_name = 'customers'

urlpatterns = [
    path('', views.CustomersIndexView.as_view(), name='index'),
    path('<int:pk>/', views.CustomersDetailView.as_view(), name='customer')
]