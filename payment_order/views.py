from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import render,get_object_or_404
from rest_framework import generics, status
from rest_framework.response import Response
from django.http import HttpResponseRedirect
from django.utils import timezone
from payment_order.models import Payment_Order

def create_payment_order(request,order_id):
    print("=========================CREATE PAYMENT=======================")
    user_id= request.session['user_id']
    amount= request.session['amount']
    method= 'cash'
    current_date = timezone.now()
    
    # Create a payment
    payment = Payment_Order(user_id=user_id, order_id=order_id, amount=amount, method=method, date=current_date)
    payment.save()
    print("==========================PAYMENT=======================")
    if payment.id:
        print("Payment saved successfully with ID:", payment.id)
    else:
        print("Failed to save payment")
    return HttpResponseRedirect('/show_orders/')