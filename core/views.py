from django.shortcuts import render

# Create your views here.
from .models import Product
from .models import Profile


def index(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'core/home-page.html', context)


def checkout(request):
    return render(request, 'core/checkout-page.html')


def productPage(request, slug):
    product = Product.objects.get(slug=slug)
    context = {'product': product}
    print(product.price)
    return render(request, 'core/product-page.html', context)


def cartPage(request):
    product = Product.objects.all()
    profile = Profile.objects.get(user=request.user)
    for i in profile.cartItem.all():
        print(i.name)
    print(request.user)

    context = {'product': product}
    return render(request, 'core/cartPage.html', context)
