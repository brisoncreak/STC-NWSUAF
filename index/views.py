from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, logout,login
from django.contrib.auth.hashers import make_password, check_password
from .models import *
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib import messages
import json
# Create your views here.
def index_views(request):

    return render(request, 'index.html')

def index_login(request):

    if request.method == 'GET':
        return redirect('/login')
    username = request.POST.get('username')
    password = request.POST.get('password')

    try:
        user = User.objects.get(username=username)
    except:
        messages.error(request,'用户名不存在')
        return HttpResponseRedirect('/')

    if check_password(password,user.password):
        request.session['username'] = user.username
        request.session.set_expiry(600)
        messages.success(request,'登录成功')
        return HttpResponseRedirect('/')
    else:
        messages.error(request,'密码错误')
        return HttpResponseRedirect('/')



def index_logout(request):
    try:
        del request.session['username']
    except:
        pass
    messages.success(request,'退出成功')
    return HttpResponseRedirect('/')


def index_register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        email = request.POST.get('email')
        if password1 == password2:
            password = make_password(password1)
            User.objects.create(username = username,password = password, email = email)
            messages.success(request,'注册成功')
            return redirect('/')
        else:
            messages.error(request,'密码错误')
            return redirect('/register')
    else:
        return redirect('/register')



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


