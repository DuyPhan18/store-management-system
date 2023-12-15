from django.shortcuts import render
from django.http import HttpResponseRedirect 
from .models import Product
from .forms import ProductForm
from django.db.models import Q
def product_list(request):
    query = request.GET.get('search')
    filterActive = request.GET.get('')
    Products = Product.objects.all().order_by('id')

    if query:
        Products = Products.filter(Q(product_name__icontains=query))

    context = {'Products': Products, 'query': query}
    
    return render(request, 'product/product.html', context)

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
    
