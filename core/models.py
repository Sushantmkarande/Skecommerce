from django.db import models
from django.shortcuts import reverse
# Create your models here.
from django.conf import settings


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
