from django.shortcuts import render
from django.http import HttpResponse
from product.models import Product
# Create your views here.
def index(request):
    Data = {'Products': Product.objects.all().order_by('id')}
    return render(request, 'pages/home.html', Data)
