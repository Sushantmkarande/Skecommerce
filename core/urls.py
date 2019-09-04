from django.urls import path, include
from .views import index
from .views import checkout
from .views import productPage
from .views import cartPage


urlpatterns = [
    path('', index, name='index'),
    path('checkout/', checkout, name='checkout'),
    path('productpage/<slug>/', productPage, name='productPage'),
    path('cart/', cartPage, name='cart')

]
