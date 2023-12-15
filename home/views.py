from django.shortcuts import render
from django.http import HttpResponseRedirect, JsonResponse
from product.models import Product
from .forms import RegisterFrom
import json
# Create your views here.
def index(request):
    Data = {'Products': Product.objects.all().order_by('id')}
    return render(request, 'pages/home.html', Data)
def Register(request):
    form = RegisterFrom()
    if request.method == 'POST':
        form = RegisterFrom(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        return render(request, 'pages/register.html', {'form':form})
def update_session(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        request.session['bill'] = data['bill']
        request.session.save()
        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'error'})