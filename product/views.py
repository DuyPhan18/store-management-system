from django.shortcuts import render,get_object_or_404, redirect
from django.http import HttpResponseRedirect
from .models import Product
from .forms import ProductForm, UpdateProductForm
from django.urls import reverse

from django.db.models import Q
def product_list(request):
    query = request.GET.get('search')
    filter_status = request.GET.get('status', '')
    Products = Product.objects.all().order_by('id')
    
    if filter_status.lower() == 'true':
        print( filter_status.lower() == 'true')
        Products = Product.objects.filter(status=True)
    elif filter_status == 'False':
        Products = Product.objects.filter(status=False)
    else:
        Products = Product.objects.all()

    if query:
        Products = Products.filter(Q(product_name__icontains=query))
 
    context = {'Products': Products,'filter_status':filter_status, 'query': query}
    
    return render(request, 'product/product.html', context)

def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = Product()
            product.add_product(form.cleaned_data)
            
            return HttpResponseRedirect('/product')  # Chuyển hướng về danh sách sản phẩm sau khi thêm
    else:
        form = ProductForm()

    return render(request, 'product/add_product.html', {'form': form})

def product_details(request, id):
    product_detail = Product.objects.get(pk=id)
   
    return render(request, 'product/product_item.html', {'product_detail': product_detail})

def update_product(request, id):
    product = get_object_or_404(Product, pk=id)
    if request.method == 'POST':
        form = UpdateProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            product.update_product(form.cleaned_data)
           
            return HttpResponseRedirect(reverse('product_detail', args=[id]))
        else:
            form = UpdateProductForm(instance=product)

    return render(request, 'product/product_item.html', {'form': form, 'product': product})

def del_product(request, id):
    product = get_object_or_404(Product, pk=id)

    if product.status:
        # Thực hiện xóa sản phẩm
        result_message = "Sản phẩm không thể xóa vì đang không bán."
       
    else:
        product.del_product()
        result_message = "Xóa sản phẩm thành công."

    # Chuyển hướng về trang sản phẩm hoặc trang chính
    return redirect('/product')