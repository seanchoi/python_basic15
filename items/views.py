from django.shortcuts import render

# Create your views here.

def electronics(request):
    product = {
        "product1": "Mac",
        "product2": "iPhone",
        "product3": "iPad",
    }
    return render(request, 'items/products.html', product)

def toys(request):
    product = {
        "product1": "Gun",
        "product2": "Doll",
        "product3": "Helicopter",
    }
    return render(request, 'items/products.html', product)

def shoes(request):
    product = {
        "product1": "Nike",
        "product2": "Addidas",
        "product3": "Reebok",
    }
    return render(request, 'items/products.html', product)

def index(request):
    return render(request, 'items/index.html')