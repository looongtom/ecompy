from calendar import c
from django.shortcuts import render
from book.models import Book
from mobile.models import Mobile
from clothe.models import Clothe

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

import json

import mobile

def show_books(request):
    books = Book.objects.all()
    mobiles = Mobile.objects.all()
    clothes = Clothe.objects.all()
    return render(request, 'home.html', {'books': books, 'mobiles': mobiles, 'clothes': clothes})

def search(request):
    query = request.GET.get('keyword')
    if query:
        results = Book.objects.filter(name__icontains=query)
    else:
        results = Book.objects.all()
    return render(request, 'home.html', {'books': results, 'query': query})

def searchByVoice(request):
    query = request.GET.get('keyword')
    if query:
        list_query = query.split(" ")
        for q in list_query:
            results = Book.objects.filter(name__icontains=q)
    else:
        results = Book.objects.all()
    return render(request, 'home.html', {'books': results, 'query': query})

@csrf_exempt
@require_POST
def searchByImage(request):
    print("=========request=======")
    print(request.body)
    data = json.loads(request.body)
    print("=========data=======")
    print(data)
    similar_images = data.get('similar_images', '')
    books = Book.objects.all()
    filer_books = []
    for book in books:
        if book.image in similar_images:
            print(book.image)
            filer_books.append(book)
        # print(book.image)
    # return render(request, 'home.html', {'books': books})
    # return JsonResponse({'similar_images': similar_images})
    return render(request, 'home.html', {'books': filer_books})

def searchByImageV2(request):
    data_json = request.GET.get('similar_images', None)
    print("=========data_json=======")
    print(data_json)
    result_data = json.loads(data_json)   
    books = Book.objects.all()
    filer_books = []
    for book in books:
        if book.image in result_data:
            filer_books.append(book)
        # print(book.image)
    print("=========filer_books size=======")
    print(len(filer_books))
    return render(request, 'home.html', {'books': filer_books})
    # # return JsonResponse({'similar_images': similar_images})
    # return render(request, 'home.html', {'books': filer_books})

    # return JsonResponse(json.dumps(result_data), safe=False)
    