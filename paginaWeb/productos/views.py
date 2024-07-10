# views.py
from django.shortcuts import render
from django.urls import reverse
from .models import Item

def index(request):
    productos_destacados = Item.objects.filter(destacado=True)[:9]
    return render(request, 'productos/index.html', {'productos_destacados': productos_destacados})


def desc_Cell1(request):
    return render(request, 'productos/desc_Cell1.html')

def compras(request):
    return render(request, 'productos/compras.html')

def desc_TV1(request):
    return render(request, 'productos/desc_TV1.html')

def desc_TV2(request):
    return render(request, 'productos/desc_TV2.html')

def desc_Cell2(request):
    return render(request, 'productos/desc_Cell2.html')

def desc_Micro1(request):
    return render(request, 'productos/desc_Micro1.html')

def desc_Micro2(request):
    return render(request, 'productos/desc_Micro2.html')

def desc_Pc1(request):
    return render(request, 'productos/desc_Pc1.html')

def desc_Pc2(request):
    return render(request, 'productos/desc_Pc2.html')

def desc_Pc3(request):
    return render(request, 'productos/desc_Pc3.html')


def my_view(request):
    login_url = reverse('login') 

