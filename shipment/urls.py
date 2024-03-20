from django.urls import path, re_path
from . import views

urlpatterns = [
    path('create_shipment/<int:order_id>/', views.create_shipment, name='create_shipment'),
    path('update_shipment/<int:shipment_id>/', views.update_shipment, name='update_shipment'),
    path('show_shipments_detail/<int:shipment_id>/', views.show_shipments_detail, name='show_shipments_detail'),
] 