from functools import wraps
from django.shortcuts import redirect
from django.http import HttpResponseNotFound

def is_authenticated(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if 'user_id' not in request.session:
            return redirect('show_login_page')  # Thay 'login' bằng tên của URL pattern của trang đăng nhập
        return view_func(request, *args, **kwargs)
    return wrapper

def is_admin(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if 'role' not in request.session:
            return redirect('show_login_page')  # Thay 'login' bằng tên của URL pattern của trang đăng nhập
        else:
            if request.session['role'] != 'ADMIN':
                return HttpResponseNotFound()
        return view_func(request, *args, **kwargs)
    return wrapper