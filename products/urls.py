from django.contrib import admin
from django.urls import path, include
from .views import index, get_product, get_category, order_by_name, order_by_availability
from products.views_test.products import ProductsList, ProductsDetail, ProductsCreate
from products.views_test.category import CategoryList, CategoryDetail, CategoryCreate

urlpatterns = [
    path('', index , name = 'index'),
    path('products/<pk>/', get_product),
    path('category/<pk>/', get_category),
    path('order_by_name', order_by_name),
    path('order_by_availability', order_by_availability),
    path('rest/products/', ProductsList.as_view()),
    path('rest/products/<pk>/', ProductsDetail.as_view()),
    path('rest/create/products/', ProductsCreate.as_view()),
    path('rest/category/', CategoryList.as_view()),
    path('rest/category/<pk>', CategoryDetail.as_view()),
    path('rest/create/category/', CategoryCreate.as_view()),
]