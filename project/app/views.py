
from django.shortcuts import render, redirect
from .models import Document
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout




def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        password_confirm = request.POST.get('password_confirm')

        if password != password_confirm:
            messages.error(request, 'Passwords do not match.')
            return render(request, 'accounts/register.html')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists.')
            return render(request, 'register.html')

        
        user = User.objects.create_user(username=username, password=password)
        user.save()
        messages.success(request, 'Registration successful. Please log in.')
        return redirect(login)
    return render(request,'register.html')
    

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Login successful.')
            return redirect(home)  
        else:
            messages.error(request, 'Invalid username or password.')

    return render(request, 'login.html')


def logout(request):
    logout(request)
    messages.success(request, 'Logout successful.')
    return redirect(login)






def home(req):
    return render(req,'home.html')

def add(req):
    return render(req,'add.html')

def view(req):
    return render(req,'view.html')

def edit(req):
    return render(req,'edit.html')

def delete(req):
    return redirect(view)