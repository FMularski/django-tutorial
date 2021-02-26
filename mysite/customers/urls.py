from django.urls import path
from . import views


app_name = 'customers'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:customer_id>/detail/', views.detail, name='detail'),
    path('<int:customer_id>/detail/orders/<int:order_id>', views.order, name='order')
]