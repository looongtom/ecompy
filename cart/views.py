from rest_framework import generics
from .serializers import CartSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import render,get_object_or_404
from book.models import Book
from mobile.models import Mobile
from clothe.models import Clothe

from .models import Cart


from rest_framework import generics, status
from rest_framework.response import Response
from .models import Cart
from .serializers import CartSerializer
from django.shortcuts import get_object_or_404
from book.models import Book 

from django.http import HttpResponseRedirect

# Create your views here.

class CartListView(APIView):
    def get(self, request):
        #get cat with status available
        cart_items = Cart.objects.filter(status='available')
        
        overall_total=0
        for cart_item in cart_items:
            overall_total += cart_item.total()

        # return render(request, 'show_cart.html', {'cart_items': cart_items})
        return render(request, 'show_cart.html', {'cart_items': cart_items, 'overall_total': overall_total})


def add_to_cart(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    # Check if the book is already in the cart and the status is available
    cart_item, created = Cart.objects.get_or_create(book=book, status='available')
    if not created:
        cart_item.quantity += 1
        cart_item.status='available'
        print("Update the quantity of the item in the cart")
        cart_item.save()
    #If the book is already in the cart and the status is  available, update the quantity
    else:
        print("Add new item to cart with status available")
        cart_item.quantity = 1
        cart_item.save()

    return HttpResponseRedirect('/cart/')
    # cart_items = Cart.objects.all()  
    # return render(request, 'show_cart.html', {'cart_items': cart_items})

def add_to_cart_mobile(request, mobile_id):
    mobile = get_object_or_404(Mobile, id=mobile_id)

    # Check if the mobile is already in the cart
    cart_item, created = Cart.objects.get_or_create(mobile=mobile, status='available')
    if not created:
        cart_item.quantity += 1
        cart_item.status='available'
        print("Update the quantity of the item in the cart")
        cart_item.save()
    #If the book is already in the cart and the status is  available, update the quantity
    else:
        print("Add new item to cart with status available")
        cart_item.quantity = 1
        cart_item.save()
    return HttpResponseRedirect('/cart/')

def add_to_cart_clothe(request, clothe_id):
    clothe = get_object_or_404(Clothe, id=clothe_id)

    # Check if the clothe is already in the cart
    cart_item, created = Cart.objects.get_or_create(clothe=clothe, status='available')

    # If the clothe is already in the cart, increase the quantity
    if not created:
        cart_item.quantity += 1
        cart_item.status='available'
        print("Update the quantity of the item in the cart")
        cart_item.save()
    #If the book is already in the cart and the status is  available, update the quantity
    else:
        print("Add new item to cart with status available")
        cart_item.quantity = 1
        cart_item.save()
    return HttpResponseRedirect('/cart/')

def update_cart_quantity(request, cart_item_id):
    if request.method == 'POST':
        new_quantity = request.POST.get('new_quantity')
        cart_item = get_object_or_404(Cart, id=cart_item_id)
        cart_item.quantity = new_quantity
        cart_item.save()
        # cart_items = Cart.objects.all()  
        # return render(request, 'show_cart.html', {'cart_items': cart_items})
        return HttpResponseRedirect('/cart/')


def delete_cart(request, cart_item_id):
    # Delete the cart item
    cart_item = get_object_or_404(Cart, id=cart_item_id)
    cart_item.delete()
    return HttpResponseRedirect('/cart/')
