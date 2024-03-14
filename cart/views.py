from rest_framework import generics
from .serializers import CartSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import render,get_object_or_404
from book.models import Book
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
        cart_items = Cart.objects.all()  
        
        overall_total=0
        for cart_item in cart_items:
            overall_total += cart_item.total()

        # return render(request, 'show_cart.html', {'cart_items': cart_items})
        return render(request, 'show_cart.html', {'cart_items': cart_items, 'overall_total': overall_total})


def add_to_cart(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    print("book.id: ")

    print(book.id)
    # Check if the book is already in the cart
    cart_item, created = Cart.objects.get_or_create(book=book)

    # If the book is already in the cart, increase the quantity
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return HttpResponseRedirect('/cart/')
    
    # cart_items = Cart.objects.all()  
    # return render(request, 'show_cart.html', {'cart_items': cart_items})


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
    cart_item = get_object_or_404(Cart, id=cart_item_id)
    cart_item.delete()
    # cart_items = Cart.objects.all()  
    # return render(request, 'show_cart.html', {'cart_items': cart_items})
    return HttpResponseRedirect('/cart/')
