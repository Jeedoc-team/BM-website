from django.shortcuts import render
from .models import *

# Create your views here.

def home(request):
    produits = Product.objects.all()[:9] 
    context = {"produits":produits}
    return render(request, "index.html", context)


def products(request):
    all_products = Product.objects.all() 
    categorie_elec = Product.objects.all().filter(categorie="Eléctricité")
    categorie_plomb = Product.objects.all().filter(categorie="Plomberie")
    categorie_mat = Product.objects.all().filter(categorie="Matériels et divers")
    return render(request, "products.html", locals())


def contact_us(request):

    return render(request, "contact.html",)


def about_us(request):

    return render(request, "about.html",)


