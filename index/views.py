from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password, check_password
from .models import *

# Create your views here.
def index_views(request):

    return render(request, 'index.html')

def index_login(request):

    if request.method == 'GET':
        return redirect('/')
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')

    try:
        user = User.objects.get(username=username)
    except:
        return HttpResponse('用户名或密码不正确')

    if check_password(password,user.password):
        return HttpResponse('登录成功')
    else:
        return HttpResponse('用户名或密码不正确')


def index_logout(request):
    logout(request)
    return redirect('/')

def signup_views(request):
    if request.method == 'GET':
        return redirect(request,'/')
    username = request.POST.get('username', '')
    password1 = request.POST.get('password1', '')
    password2 = request.POST.get('password2', '')
    email = request.POST.get('email', '')
    if password1 == password2:
        password = make_password(password1)
        User.objects.create(username = username, \
        password = password, mobile = mobile, \
        email = email)
        return HttpResponse('注册成功')
    else:
        return HttpResponse('两次密码不一致')



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

