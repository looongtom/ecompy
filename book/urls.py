from django.urls import path, re_path
from . import views
from .views import AddBookView
from .views import UpdateBookViewV2
from .views import DeleteBookView


urlpatterns = [ 
    # path('', views.ListBookView.as_view(), name='API to get list of book'),
    path('book-list/', views.ListBookView.as_view(), name='book-list'),
    
    path('add-book/', AddBookView.as_view(), name='add-book'),

    path('update-book-v2/<int:pk>/', UpdateBookViewV2.as_view(), name='update-book-v2'),

    path('delete-book/<int:pk>/', DeleteBookView.as_view(), name='delete-book'),

    path('<int:id>', views.UpdateBookView.as_view(), name='API to update book'),
 

]