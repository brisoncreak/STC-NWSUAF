from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def index_views(request):

    return render(request,'index.html')

def index_login(request):
    if request.method == 'GET':
        return render(request, 'login.html')

    username = request.POST.get('username', '')
    password = request.POST.get('password', '')

    user = authenticate(request, username=username, password=password)
    if user:
        login(request, user)
    return redirect('/')

def index_logout(request):
    logout(request)
    return redirect('/')