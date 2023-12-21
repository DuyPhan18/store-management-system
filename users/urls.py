from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.user_list, name='user_list'),
    path('<int:id>/', views.user_info, name='user_info'),
    path('update_user/<int:id>/', views.update_user, name='update_user'),
    path('delete_user/<int:id>/', views.delete_user, name='delete_user'),
]