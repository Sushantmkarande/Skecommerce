from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.contrib import messages

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
    return render(request, 'core/product-page.html', context)


def cartPage(request):
    # print(request.user.is_authenticated)
    if request.user.is_authenticated:

        profile = Profile.objects.get(user=request.user)
        context = {'cartitems': profile.cartItem.all()}
        return render(request, 'core/cartPage.html', context)
    else:
        messages.info(request, 'You are not logged in')
        return render(request, 'core/cartPage.html')


def addtocart(request, slug):
    item = Product.objects.get(slug=slug)
    profile = Profile.objects.get(user=request.user)
    profile.cartItem.add(item)
    messages.info(request, 'item added to carts')
    return redirect('productPage', slug=slug)
