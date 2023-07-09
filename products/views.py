from django.shortcuts import render
from .models import Products, Category

# Create your views here.


def index(request):
    p = Products.objects.all() # select * from products

    return render(request,'products/index.html', {'products': p,})   

def get_product(request, pk):
    p = Products.objects.get(pk=pk) # select * from products where pk = 2

    return render(request,'products/product.html', {'p': p,})

def get_category(request, pk):
    p = Products.objects.filter(category_id=pk)
    
    return render(request,'products/category.html', {'products': p,})

def order_by_name(request):
    p = Products.objects.all().order_by('name')
    
    return render(request,'products/index.html', {'products': p,})

def order_by_availability(request):
    p = Products.objects.filter(is_available=1)
    
    return render(request,'products/index.html', {'products': p,})