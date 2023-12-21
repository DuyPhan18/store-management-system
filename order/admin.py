from django.contrib import admin
from .models import Order, OrderDetails

class OrderDetailsInline(admin.TabularInline):
    model = OrderDetails

class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderDetailsInline]

admin.site.register(Order, OrderAdmin)
admin.site.register(OrderDetails)