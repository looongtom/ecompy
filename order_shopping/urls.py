from django.contrib import admin
from . import views
from django.urls import path

urlpatterns = [
    path('', views.show_orders, name='show_orders'),
    path('show_order_details/<int:order_id>/', views.show_order_details, name='show_order_details'),
    path('create_order/', views.create_order, name='create_order'),
    
]