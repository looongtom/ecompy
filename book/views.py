from django.shortcuts import render, redirect

from django.http import JsonResponse

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
import urllib
from urllib import parse
from .models import Book
from .serializers import BookSerializer
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from .forms import BookForm
from person_project.decorator import(
    is_authenticated,
    is_admin
) 
from django.utils.decorators import method_decorator
from rest_framework import generics

# Create your views here.
# class BookCreateView(generics.CreateAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
class DeleteBookView(DeleteView):
    model = Book
    template_name = 'delete_book.html'
    success_url = reverse_lazy('book-list')
class UpdateBookViewV2(UpdateView):
    model = Book
    form_class = BookForm

    # fields = ['name','image', 'author','price','description']  # Add other fields as needed
    template_name = 'update_book.html'
    success_url = reverse_lazy('book-list')
class AddBookView(CreateView):
    model = Book
    form_class = BookForm
 
    # fields = ['name','image' ,'author','price','description']  # Add other fields as needed
    template_name = 'add_book.html'
    success_url = reverse_lazy('book-list') 
class ListBookView(APIView):
    @method_decorator(is_authenticated)
    @method_decorator(is_admin)
    def get(self, request, format=None):
        user_id = request.session.get('user_id')
        if not user_id:
            # request.session['previous_request'] = 
            return redirect('show_login_page')
        else:
            print("================request.session=====================")
            print(request.session['user_id'])
            # book = Book.objects.all()
            book = Book.objects.prefetch_related('categories').all()
            # print("=====================================")
            # for b in book:
            #     print(b.name)
            #     for c in b.categories.all():
            #         print(c.name)        
            # print("=====================================")
            
            serializer = BookSerializer(book, many=True)
            # return Response(serializer.data)
            return render(request, 'book_list.html', {'books':book})

    # @is_authenticated
    # @is_admin  
    def post(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({
                'message': 'Create a new book successfully'
            }, status = status.HTTP_201_CREATED)
        else:
            return JsonResponse({
                'message': 'Create a new book unsuccessfully'
            }, status = status.HTTP_400_BAD_REQUEST)
# put and delete book
class UpdateBookView(APIView):  
    # @is_authenticated
    # @is_admin  
    def get(self, request, id):
        # ids  = request.GET.get('id')
        # name = parse.unquote(name)
        BookById = Book.objects.filter(id=id)
        serializer = BookSerializer(BookById, many=True)
        return Response(serializer.data)
    # @is_authenticated
    # @is_admin  
    def delete(self, request,id ,*args, **kwargs):
        # name  = request.GET.get('id')
        # name = parse.unquote(name)
        print(id)
        book = Book.objects.filter(id=id)
        book.delete()
        return JsonResponse({
                'message': 'Delete book successfully'
            }, status = status.HTTP_204_NO_CONTENT)    
    # @is_authenticated
    # @is_admin      
    def put(self, request, id):
        # name = request.GET.get('id')
        # name = parse.unquote(name)
        book = Book.objects.get(id=id)
        serializer = BookSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({
                'message': 'Update book successfully'
            }, status = status.HTTP_201_CREATED)
        else:
            return JsonResponse({
                'message': 'Update unsuccessfully'
            }, status = status.HTTP_400_BAD_REQUEST)     
