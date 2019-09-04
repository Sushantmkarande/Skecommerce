from django.contrib import admin

# Register your models here.
from .models import Product
from .models import Profile

admin.site.register(Product)
admin.site.register(Profile)
