from django.shortcuts import render
import cart
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import render,get_object_or_404
from .models import Order, OrderItem
from book.models import Book
from mobile.models import Mobile
from clothe.models import Clothe
from cart.models import Cart
from rest_framework import generics, status
from rest_framework.response import Response
from .serializers import OrdersSerializer
from django.http import HttpResponseRedirect

from django.utils import timezone

def show_orders(request):
    list_orders = Order.objects.all()
    return render(request, 'show_orders.html', {'list_orders': list_orders})

def show_order_details(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    order_items = OrderItem.objects.filter(order_id=order_id)
    cart=Cart.objects.filter(order_id=order_id)
    list_books_in_order = []
    list_mobiles_in_order = []
    list_clothes_in_order = []
    for order_item in order_items:
        if order_item.book_id:
            book = get_object_or_404(Book, id=order_item.book_id)
            list_books_in_order.append(book)
        if order_item.mobile_id:
            mobile = get_object_or_404(Mobile, id=order_item.mobile_id)
            list_mobiles_in_order.append(mobile)
        if order_item.clothe_id:
            clothe = get_object_or_404(Clothe, id=order_item.clothe_id)
            list_clothes_in_order.append(clothe)
    return render(request, 'show_order_details.html', {'order': order, 'order_items': order_items, 'list_books_in_order': list_books_in_order, 'list_mobiles_in_order': list_mobiles_in_order, 'list_clothes_in_order': list_clothes_in_order, 'cart': cart})

def create_order(request):
    # Get items from the cart with status "available"
    user_id= request.session['user_id']
    cart_items = Cart.objects.filter(status='available')
    overall_total=0
    for cart_item in cart_items:
        overall_total += cart_item.total()
    current_date = timezone.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S.%f")    
    print("ORDER=======================")
    print(user_id, overall_total, current_date)
    
    # Create an order
    order = Order(user_id=user_id, total=overall_total, date=current_date, status='pending')
    order.save()
    if order.id:
        print("Order saved successfully with ID:", order.id)
    else:
        print("Failed to save order")
    
    book_id, mobile_id, clothe_id = None, None, None
    if cart_item.book_id:
        book_id = cart_item.book_id
    if cart_item.mobile_id:
        mobile_id = cart_item.mobile_id
    if cart_item.clothe_id:
        clothe_id = cart_item.clothe_id

    for cart_item in cart_items:
        order_item = OrderItem(order_id=order.id, cart=cart_item)
        order_item.save()
    
    #  Change the status of the cart items to "ordered"
    for cart_item in cart_items:
        cart_item.status = 'ordered'
        cart_item.save()
    return HttpResponseRedirect('/orders/')
    
def pay_order(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    order.status = 'paid'
    order.save()
    #call api to create shipment

    return HttpResponseRedirect('/orders/')