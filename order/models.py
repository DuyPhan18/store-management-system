from django.db import models
from product.models import Product
from django.contrib.auth.models import User
# Create your models here.
def get_current_user():
    # Trả về người dùng hiện tại đang đăng nhập
    # Bạn cần chắc chắn rằng có một người dùng đang đăng nhập khi gọi hàm này
    return User.objects.get(username='duyph').id
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=get_current_user)
    customer_name = models.CharField(max_length=30)
    total_bill =  models.DecimalField(max_digits=30, decimal_places=2)
    total_quantity = models.IntegerField(default=0)
    date = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return f"Order #{self.id} - {self.product_info.product_name}"
    

class OrderDetails(models.Model):
    order = models.ForeignKey(Order, related_name='products', on_delete=models.CASCADE)
    product_name = models.CharField(max_length=255)
    quantity = models.IntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)  
