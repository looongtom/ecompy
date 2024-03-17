from django.shortcuts import render, redirect
from .models import (
    User
)
from .serializers import (
    UserJson
)
from rest_framework.response import Response
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from django.contrib.auth.hashers import make_password, check_password
from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist

def show_login_page(request):
    return render(request, 'login.html')

def show_register_page(request):
    return render(request, 'register.html')

@csrf_exempt
@api_view(['POST'])
def login(request):
    email = request.data.get('email')
    password = request.data.get('password')

    try:
        user = User.objects.get(email=email)
    except ObjectDoesNotExist:
        return Response({'error': 'Tên đăng nhập hoặc mật khẩu không chính xác'}, status=status.HTTP_401_UNAUTHORIZED)

    if check_password(password, user.password):
        # Lưu thông tin user vào session
        request.session['user_id'] = user.id
        request.session['username'] = user.email
        request.session['fullname'] = user.full_name
        request.session['role'] = user.role

        return Response({'message': 'Đăng nhập thành công'}, status=status.HTTP_200_OK)
    else:
        return Response({'error': 'Tên đăng nhập hoặc mật khẩu không chính xác'}, status=status.HTTP_401_UNAUTHORIZED)

@api_view(['POST'])
@csrf_exempt
def registration(request):
    userJson = UserJson(data=request.data, context={'request': request})
    print(userJson)
    if userJson.is_valid():
        validated_data = userJson.validated_data  # Lấy dữ liệu đã được xác thực
        validated_data['password'] = make_password(validated_data['password'])  # Băm mật khẩu
        validated_data['role'] = 'USER'  # Gán giá trị cho trường role
        userJson.save()  # Lưu vào cơ sở dữ liệu
        return Response(status=status.HTTP_200_OK)
    else:
        print("---------------------NOT VALID-------------------")
        print(userJson.validated_data)

        return Response(userJson.errors, status=status.HTTP_400_BAD_REQUEST)
    
def logout(request):
    request.session.clear()
    return redirect('show_login_page') 