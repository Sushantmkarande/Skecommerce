from django.contrib import admin

# Register your models here.
<<<<<<< HEAD
from .models import Product
from .models import Profile

admin.site.register(Product)
admin.site.register(Profile)
=======
from .models import Order, OrderItem, Item

admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Item)
>>>>>>> cda2804d284b606591f93b36e6b7d59e130c9377
