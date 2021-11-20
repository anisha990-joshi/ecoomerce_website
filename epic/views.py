from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

from .category import Category
from .customer import Customer

from .models import *
def products(request):
    productss = Product.objects.all()
    return render(request, 'products.html', {'productss':productss})
def home(request):
    return render(request,'pink.html')
def customer(request):
    customerr =  Customer.objects.all()
    return render(request,'customer.html',{'customerr':customerr})
def category(request):
    categories = Category.objects.all()
    return render(request,'category.html',{'categories':categories})


def black_shoe(request):
    return render(request,'black_shoe.html', {'i': 'http://127.0.0.1:8000'})
