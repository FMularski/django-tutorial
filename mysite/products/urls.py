from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    path('', views.ProductsIndexView.as_view(), name='index'),
    path('<int:pk>/', views.ProductsDetailView.as_view(), name='detail')
]
