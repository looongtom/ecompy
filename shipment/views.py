from django.shortcuts import render
from django.utils import timezone
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import render,get_object_or_404
from .models import Shipment
from rest_framework import generics, status
from rest_framework.response import Response
from django.http import HttpResponseRedirect
from .serializers import ShipmentSerializer
from order_shopping.models import Order
# Create your views here.
def create_shipment(request,order_id):
    order = get_object_or_404(Order, id=order_id)
    order.status = 'paid'
    order.save()

    user_id= request.session['user_id']
    #get order_id from the request
    date = timezone.now()
    status='delivering'
    shipment = Shipment(user_id=user_id, order_id=order_id, address='', date=date, status=status)
    shipment.save()
    return render(request, 'create_shipment.html', {'shipment': shipment})

def update_shipment(request,shipment_id):
    shipment = get_object_or_404(Shipment, id=shipment_id)
    shipment.address= request.POST['address']
    shipment.save()
    order = get_object_or_404(Order, id=shipment.order_id)
    request.session['amount'] = shipment.ship_fee+order.total
    #redirect to create_payment with order_id from app payment 
    return HttpResponseRedirect('/payment_order/create_payment_order/'+str(shipment.order_id))
    


def show_shipments_detail(request,shipment_id):
    shipment= get_object_or_404(Shipment, id=shipment_id)
    return render(request, 'show_shipments_detail.html', {'shipment': shipment})