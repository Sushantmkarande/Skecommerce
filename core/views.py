from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.contrib import messages

# Create your views here.
from .models import Product
from .models import Profile

from .forms import myForm, cartForm, ProductForm


def test(request):
    # form = myForm()
    form1 = cartForm()
    form2 = ProductForm()
    context = {'form1': form1, 'form2': form2}
    return render(request, 'core/test.html', context)


def index(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'core/home-page.html', context)


def checkout(request):
    print(request.POST)
    return render(request, 'core/checkout-page.html')


def productPage(request, slug):
    product = Product.objects.get(slug=slug)
    context = {'product': product}
    return render(request, 'core/product-page.html', context)


def cartPage(request):
    print(request.POST)
    # print(request.user.is_authenticated)
    if request.user.is_authenticated:

        profile = Profile.objects.get(user=request.user)
        context = {'cartitems': profile.cartItem.all()}

        return render(request, 'core/cartPage.html', context)
    else:
        messages.info(request, 'You are not logged in')
        return render(request, 'core/cartPage.html')


def addToCart(request, slug):
    item = Product.objects.get(slug=slug)
    profile = Profile.objects.get(user=request.user)
    profile.cartItem.add(item)
    messages.info(request, 'item added to carts')
    return redirect('productPage', slug=slug)


def removeFromCart(request, slug):
    item = Product.objects.get(slug=slug)
    profile = Profile.objects.get(user=request.user)
    profile.cartItem.remove(item)
    messages.info(request, 'item deleted from carts')
    return redirect('cart')
