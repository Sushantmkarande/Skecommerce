from django.urls import path, include
from .views import index
from .views import checkout
from .views import productPage
from .views import cartPage
from .views import test

from .views import addToCart
from .views import removeFromCart


urlpatterns = [
    path('', index, name='index'),
    path('checkout/', checkout, name='checkout'),
    path('productpage/<slug>/', productPage, name='productPage'),
    path('cart/', cartPage, name='cart'),
    path('addToCart/<slug>', addToCart, name='addToCart'),
    path('removeToCart/<slug>', removeFromCart, name='removeFromCart'),
    path('test/', test, name='test')
]
