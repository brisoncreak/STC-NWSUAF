from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .models import *

# Create your views here.
def index_views(request):

    return render(request, 'index.html')

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



def test(request):
    if request.method == 'GET':
        return render(request, 'test.html')
    a = request.POST.get('list')
    print(a)
    return render(request, 'test.html')

def index_modelbase(request):
    nongke = Collegetype.objects.get(title='农科')
    colleges_nongke = Colleges.objects.filter(classify_id=nongke.id)    
    gongke = Collegetype.objects.get(title='工科')
    colleges_gongke = Colleges.objects.filter(classify_id=gongke.id)
    like = Collegetype.objects.get(title='理科')
    colleges_like = Colleges.objects.filter(classify_id=like.id)
    wenke = Collegetype.objects.get(title='文科')
    colleges_wenke = Colleges.objects.filter(classify_id=wenke.id)

    return render(request,'modelbase.html',locals())

