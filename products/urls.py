from django.contrib import admin
from django.urls import path, include
from .views import index, get_product, get_category, order_by_name, order_by_availability

urlpatterns = [
    path('', index , name = 'index'),
    path('products/<pk>/', get_product),
    path('category/<pk>/', get_category),
    path('order_by_name', order_by_name),
    path('order_by_availability', order_by_availability),
]