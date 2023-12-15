from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.order, name = 'order'),
    path('create_order/', views.create_order, name='create_order'),
    path('order_details/<int:id>/', views.order_details, name='order_details'),
]