from django.urls import path
from . import views

app_name = 'orders'

urlpatterns = [
    path('', views.OrdersIndexView.as_view(), name='index'),
    path('<int:pk>/', views.OrdersDetailView.as_view(), name='detail')
]
