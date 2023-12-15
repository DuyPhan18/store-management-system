from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect , HttpResponseNotFound
from .models import Order, OrderDetails
from product.models import Product
# Create your views here.
def order(request):
    Orders = Order.objects.all().order_by('id')
    context = {'Orders': Orders}

    return render(request, 'order/order.html', context)

def create_order(request):
    if request.method == "POST":
        user = request.user
        customer_name = request.POST.get("customer_name")
        total_bill = request.POST.get('total_bill')
        total_quantity = request.POST.get('total_quantity')

        order = Order.objects.create(
            user=user,
            customer_name=customer_name,
            total_bill=total_bill,
            total_quantity = total_quantity,
        )
        for pd_id, product_info in request.session.get('bill', {}).items():
            try:
                product_name = product_info['selectedName']
                quantity = product_info['quantity_choose']
                total_price = product_info['total_price']
                print(f"Product Name: {product_name}, Quantity: {quantity}, Total Price: {total_price}")
                OrderDetails.objects.create(
                    order=order,
                    product_name=product_name,
                    quantity=quantity,
                    total_price=total_price,
                )
            except Exception as e:
                print(f"Error creating OrderDetails: {e}")
        # Xóa 'bill' khỏi session
        if 'bill' in request.session:
            del request.session['bill']

        return HttpResponseRedirect('/')

    else:
        return render(request, 'pages/home.html')


def order_details(request, id):
    order = get_object_or_404(Order, id = id)
    order_details = OrderDetails.objects.filter(order=order)
    return render(request, 'order/order_details.html', {'order': order, 'order_details': order_details})           
