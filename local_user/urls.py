from django.contrib import admin
from . import views
from django.urls import path

urlpatterns = [
    path('login', views.login, name='login'), #name là biến được gọi đến khi sử dụng url
    path('registration', views.registration, name='registration'),
    path('login-page', views.show_login_page, name='show_login_page'),
    path('register-page', views.show_register_page, name='show_register_page'),
    path("logout", views.logout, name="logout")
]