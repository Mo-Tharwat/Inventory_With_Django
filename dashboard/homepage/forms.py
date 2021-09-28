#Step 15; Prepare forms.py at homepage App
from django import forms
from .models import *

#Step 15;Create Product form 
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields=['name','category','quantity']

#Step 17;Create Order form
class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields=['product','order_quantity']

