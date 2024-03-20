from django.urls import path, re_path
from . import views


urlpatterns = [
    path('create_payment_order/<int:order_id>/', views.create_payment_order, name='create_payment_order'),
] 