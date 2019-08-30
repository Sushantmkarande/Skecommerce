from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'core/home-page.html')


def checkout(request):
    return render(request, 'core/checkout-page.html')

def productPage(request):
    return render(request, 'core/product-page.html')
