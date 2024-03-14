from django.urls import path, re_path
from . import views
from .views import AddMobileView

urlpatterns = [ 
    path('mobile-list/', views.ListMobileView.as_view(), name='mobile-list'),
    
    path('add-mobile/', AddMobileView.as_view(), name='add-mobile'),

    path('update-mobile/<int:pk>/', views.UpdateMobileView.as_view(), name='update-mobile'),

    path('delete-mobile/<int:pk>/', views.DeleteMobileView.as_view(), name='delete-mobile'),
]