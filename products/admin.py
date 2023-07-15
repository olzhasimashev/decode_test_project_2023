from django.contrib import admin
from .models import Products, Category
# Register your models here.
# admin.site.register(Products)
admin.site.register(Category)

class ProductsAdmin (admin.ModelAdmin):
    list_display = ('name', 'description', 'price', 'date', 'category')
    list_filter = ('price', 'date', 'category')
    search_fields = ['name']

admin.site.register(Products, ProductsAdmin)

admin.site.site_header = "Aдмин панель о товарах"
admin.site.site_title = "Aдмин панель сайта"