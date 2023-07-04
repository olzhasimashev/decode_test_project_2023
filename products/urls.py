from django.contrib import admin
from django.urls import path, include
from .views import index, get_product

urlpatterns = [
    path('', index , name = 'index'),
    path('<pk>/', get_product),
]