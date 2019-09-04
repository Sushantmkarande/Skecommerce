from django.db import models
from django.shortcuts import reverse
# Create your models here.
from django.conf import settings


<<<<<<< HEAD
class Product(models.Model):
    Cat_Choise = (
        ('shirts', 'shirts'),
        ('sportware', 'sportware'),
        ('outwears', 'outwears'),
    )
    name = models.CharField(max_length=50)
    price = models.FloatField()
    category = models.CharField(max_length=30, choices=Cat_Choise)
    slug = models.SlugField(unique=True)
    img = models.ImageField(upload_to='img', max_length=200)

    def get_abs_url(self):
        return reverse("productPage", kwargs={
            'slug': self.slug
        })


class Profile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    cartItem = models.ManyToManyField(Product, blank=True)
=======
class Item(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField()

    def __str__(self):
        return self.title


class OrderItem(models.Model):
    itme = models.ForeignKey(Item, on_delete=models.CASCADE)


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    item = models.ManyToManyField(OrderItem)
    start_data = models.DateTimeField(auto_now=True)
    ordered_data = models.DateTimeField()

    def __str__(self):
        return self.user.username
>>>>>>> cda2804d284b606591f93b36e6b7d59e130c9377
