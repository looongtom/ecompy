from django.urls import path, re_path
from . import views


urlpatterns = [
    path('create_payment/<int:order_id>/', views.create_payment, name='create_payment'),
] 