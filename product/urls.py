from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('add_product/', views.add_product, name='add_product'),
    path('<int:id>/', views.product_details, name='product_detail'),
    path('delete_product/<int:id>/', views.del_product, name='delete_product'),
    path('update_product/<int:id>/', views.update_product, name='update_product'),
]