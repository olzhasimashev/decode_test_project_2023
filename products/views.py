from django.shortcuts import render
from .models import Products

# Create your views here.


def index(request):
    p = Products.objects.all() # select * from products

    return render(request,'products/index.html', {'products': p,})   

def get_product(request,pk):
    p = Products.objects.get(pk=pk) # select * from products where pk = 2

    return render(request,'products/product.html', {'p': p,})