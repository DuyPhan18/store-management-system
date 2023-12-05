# trong file forms.py
from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['product_name', 'product_desc', 'product_price', 'product_quantity', 'product_category', 'product_image']
