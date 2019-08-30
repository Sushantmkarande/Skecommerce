from django.urls import path, include
from .views import index
from .views import checkout
from .views import productPage


urlpatterns = [
    path('', index, name='index'),
    path('checkout/', checkout, name='checkout'),
    path('productpage/', productPage, name='productPage')

]
