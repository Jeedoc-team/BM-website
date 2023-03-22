from django.shortcuts import render
from .models import *

# Create your views here.

def home(request):
    produits = Product.objects.all()[:9] 
    context = {"produits":produits}
    return render(request, "index.html", context)


def products(request):
    produits = Product.objects.all() 
    context = {"produits":produits}
    return render(request, "products.html", context)


def contact_us(request):

    return render(request, "contact.html",)


def about_us(request):

    return render(request, "about.html",)


