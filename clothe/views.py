from django.shortcuts import render
from django.http import JsonResponse

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
import urllib
from urllib import parse
from .models import Clothe
from django.urls import reverse_lazy
from .forms import ClotheForm
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from rest_framework import generics
from person_project.decorator import(
    is_authenticated,
    is_admin
) 
from django.utils.decorators import method_decorator
# Create your views here.
class ListClotheView(APIView):
    @method_decorator(is_authenticated)
    @method_decorator(is_admin)
    def get(self, request, format=None):
        clothe = Clothe.objects.all()
        return render(request, 'clothe_list.html', {'clothes':clothe})

class AddClotheView(CreateView):
    model = Clothe
    form_class = ClotheForm
    template_name = 'add_clothe.html'
    success_url = reverse_lazy('clothe-list') 
    # fields = ['name','image' ,'brand','price','description']  # Add other fields as needed

class UpdateClotheView(UpdateView):
    model = Clothe
    form_class = ClotheForm
    template_name = 'update_clothe.html'
    success_url = reverse_lazy('clothe-list')