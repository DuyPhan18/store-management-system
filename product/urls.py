from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.product_list),
    path('add_product/', views.add_product, name='add_product'),
    path('<int:id>/', views.product_details),
]