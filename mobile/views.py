from django.shortcuts import render, redirect

from django.http import JsonResponse

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
import urllib
from urllib import parse
from .models import Mobile
from django.urls import reverse_lazy
from .forms import MobileForm
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from .serializers import MobileSerializer
from person_project.decorator import(
    is_authenticated,
    is_admin
) 
from django.utils.decorators import method_decorator

class ListMobileView(APIView):
    @method_decorator(is_authenticated)
    @method_decorator(is_admin)
    def get(self, request, format=None):
        mobile = Mobile.objects.all()
    
        serializer = MobileSerializer(mobile, many=True)
        return render(request, 'mobile_list.html', {'mobiles':mobile})

class AddMobileView(CreateView):
    model = Mobile
    form_class = MobileForm
  
    template_name = 'add_mobile.html'
    success_url = reverse_lazy('mobile-list')

class UpdateMobileView(UpdateView):
    model = Mobile
    form_class = MobileForm
  
    template_name = 'update_mobile.html'
    success_url = reverse_lazy('mobile-list')

class DeleteMobileView(DeleteView):
    model = Mobile
    template_name = 'delete_mobile.html'
    success_url = reverse_lazy('mobile-list')