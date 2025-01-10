from django.shortcuts import render, redirect
from django.contrib.auth import logout


def login_user(request):
    if request.method == 'GET':
        return render(request, 'user/login/login.html')

def logout_user(request):
    if request.method == 'POST' and request.user.is_authenticated:
        logout(request)

    return redirect('core:index')

    
