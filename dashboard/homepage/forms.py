#Step 15; Prepare forms.py at homepage App
from django import forms
from .models import *

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields=['name','category','quantity']

