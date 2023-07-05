from django.contrib import admin
from django.urls import path, include
from .views import index, get_product, get_category

urlpatterns = [
    path('products', index , name = 'index'),
    path('products/<pk>/', get_product),
    path('<pk>/', get_category),
]