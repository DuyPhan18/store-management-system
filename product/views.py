from django.shortcuts import render
from django.http import HttpResponseRedirect 
from .models import Product
from .forms import ProductForm
from django.views.generic import ListView, DetailView

def product_list(request):
    Data = {'Products': Product.objects.all().order_by('-date')}
    return render(request, 'product/product.html', Data)

def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/product')  # Chuyển hướng về danh sách sản phẩm sau khi thêm
    else:
        form = ProductForm()

    return render(request, 'product/add_product.html', {'form': form})

def product_details(request, id):
    product_detail = Product.objects.get(id=id)
    return render(request, 'product/product_item.html', {'product_detail': product_detail})
    
