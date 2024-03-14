from django.urls import path
from .views import show_books,search,searchByImage,searchByImageV2,searchByVoice

urlpatterns = [
    path('home/', show_books, name='show_books'),
    path('search/', search, name='search'),
    path('search_by_image/', searchByImage, name='search_by_image'),
    path('search_by_imageV2/', searchByImageV2, name='search_by_imageV2'),
    path('search_by_voice/', searchByVoice, name='search_by_imageV2'),

    # other url patterns...
]