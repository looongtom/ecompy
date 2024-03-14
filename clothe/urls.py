from django.urls import path, re_path
from . import views
from .views import AddClotheView
from .views import UpdateClotheView
urlpatterns = [
    path('clothe-list/', views.ListClotheView.as_view(), name='clothe-list'),
    path('add-clothe/', AddClotheView.as_view(), name='add-clothe'),
    path('update-clothe/<int:pk>/', UpdateClotheView.as_view(), name='update-clothe'),
]