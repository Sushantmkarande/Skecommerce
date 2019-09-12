from django import forms
from .widgets import PlusMinusNumberInput
from .models import Product, Profile


class myForm(forms.Form):
    quantity = forms.CharField(widget=PlusMinusNumberInput())


class cartForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['cartItem']


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price']
