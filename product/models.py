from django.db import models

# Create your models here.
class Product(models.Model):
    product_name = models.CharField(max_length=100)
    product_desc = models.TextField()
    product_price = models.DecimalField(max_digits = 10, decimal_places=2)
    product_quantity = models.IntegerField(default=0)
    product_category = models.CharField(max_length=100)
    product_image = models.ImageField(null=True)
    date = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)
    def __str__(self):
        return self.product_name