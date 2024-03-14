from django.urls import path, re_path
from . import views

from .views import add_to_cart,update_cart_quantity,delete_cart


urlpatterns = [
    path('', views.CartListView.as_view(), name='show_cart'),
    path('add_to_cart/<int:book_id>/', add_to_cart, name='add_to_cart'),
    path('update-cart-quantity/<int:cart_item_id>/', update_cart_quantity, name='update_cart_quantity'),
    path('delete-cart/<int:cart_item_id>/', delete_cart, name='delete-cart'),
] 