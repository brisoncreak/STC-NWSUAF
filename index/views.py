from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, logout,login
from django.contrib.auth.hashers import make_password, check_password
from .models import *
from chat.models import *
from share.models import *
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.core.mail import send_mail
from STC_NWSUAF.tools import login_required
import os
from dwebsocket import require_websocket
from bs4 import BeautifulSoup
import json
from index.models import Notification

# Create your views here.
def index_views(request):

    return render(request, 'index.html')

#登录
def index_login(request):

    if request.method == 'GET':
        return redirect('/login')
    username = request.POST.get('username')
    password = request.POST.get('password')
    isremember=request.POST.get('rem')
    try:
        user = User.objects.get(username=username)
    except:
        return HttpResponseRedirect('/')

    if check_password(password,user.password):
        a=check_password(password,user.password)
        request.session['username'] = user.username
        request.session.set_expiry(7200)
        #选择记住我创建cookie
        if isremember=='on':
            response= HttpResponseRedirect('/')
            response.set_cookie("username",user.username,3600)
            return response
        else:
            return HttpResponseRedirect('/')
    else:
        return redirect('/')


#退出
def index_logout(request):
    try:
        del request.session['username']
    except:
        pass
    return HttpResponseRedirect('/')

#注册
def index_register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        user=User.objects.all()

        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        email = request.POST.get('email')
        for u in user:
            if(username==u.username):
                return redirect('/')
            elif(email==u.email):
                return redirect('/')
        if password1 == password2 and username!='' and email!='' and password1!='':
            password = make_password(password1)
            user = User.objects.create(username = username,password = password, email = email)
            request.session['username'] = user.username
            request.session.set_expiry(7200)
            return redirect('/')
        else:
            return redirect('/')
    else:
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
#发送邮件重置密码
def index_reset(request):
    if request.method=='POST':
        username=request.POST.get('username')
        if username == '':
            return HttpResponseRedirect('/')
        else:
            user=User.objects.get(username=username)
            password=user.password
            password=password.replace('pbkdf2_sha256$36000$','a')
            send_mail("找回密码", "亲爱的用户"+username+'请点击此链接来修改你的密码,http://172.29.7.228:8000/back/reset?str1='+password+'&user='+username, "1441335655@qq.com", [user.email], fail_silently=False)
            messages.info(request,'请查看你的邮箱') 
            return HttpResponseRedirect('/')
    else:
        return redirect('/reset')
#邮件回执
def index_back(request):
    if request.method=='GET':
        password=request.GET.get('str1')
        password=password.replace(' ','+')
        username=request.GET.get('user')
        user=User.objects.get(username=username)
        user.password=password.replace('pbkdf2_sha256$36000$','a')
        if str(password) == str(user.password):
            return render(request,'back_reset.html',locals())
        else:
            messages.warning(request,'没有权限')
            return HttpResponseRedirect('/')
    else:
        username=request.POST.get('username')
        password1=request.POST.get('password1')
        password2=request.POST.get('password2')
        if password1!=password2:
            messages.error(request,'两次密码不一致')
            return HttpResponse('密码不一致')
        user=User.objects.get(username=username)
        password = make_password(password1)
        user.password=password
        user.save()
        return HttpResponseRedirect('/')

@login_required
def notify_views(request):
    user = User.objects.get(username=request.session.get('username'))
    notis = Notification.objects.filter(aim_user=user).order_by('-create_time')
    page_now = request.GET.get('page')
    if not page_now:
        page_now = 1

    page_now = int(page_now)

    count_per_page = 5
    page_sum = len(notis)//count_per_page+1
    page_range = range(1, page_sum+1)

    #计算起始位置
    start_page = (page_now-1)*count_per_page
    #创建数据集
    notis = notis[start_page:start_page+count_per_page]


    return render(request,'notification.html',locals())


@require_websocket
def ws_views(request):
    for message in request.websocket:
        if message == b'123':
            #request.websocket.send(b'456')
            #print(message)
            html = render(request, 'index.html').content
            bs = BeautifulSoup(html, "html.parser")
            noti_div = bs.find('div', id='header-bottom-right').find('div', id='rec')

            request.websocket.send(noti_div.encode('utf-8'))

# 点赞方面的函数　　包括文章点赞和文件点赞
from django.views.decorators.csrf import csrf_exempt
@csrf_exempt

#好评　isGood = True
def admire_goodnum_views(request):
    if request.method == 'POST':
        uid = request.POST.get('userID')  
        good_content = request.POST.get('goodINPUT')
        good_id = request.POST.get('goodID')   #文件的id
        admireType = request.POST.get('admireType')
        isAdd = request.POST.get('isAdd')
        user = User.objects.get(username=request.session['username'])
        file=File.objects.get(id=good_id)
        user1=User.objects.get(id=file.user_id)
        if admireType == 'file':
            File.objects.filter(id=good_id).update(file_beadmired = good_content)
            if isAdd=='1':
                Admirelog.objects.create(uid_id=uid,fid_id=good_id,isGood=True,isFile=True) #,fid_id=-1
                n = Notification(aim_user=user1, arg0=6, arg4=user)
                n.save()
            else:
                Admirelog.objects.get(isGood = True,uid_id=uid,fid_id=good_id).delete() #,fid_id=-1
            return HttpResponseRedirect('/share')
        else:
            Article.objects.filter(id=good_id).update(beadmired_num=good_content)
            if isAdd=='1':
                Admirelog.objects.create(uid_id=uid,aid_id=good_id,isGood=True,isFile=False) #,fid_id=-1
            # isadd = '0'  代表取消点赞　　　所以应该将　isGood为１　的删除
            else:
                Admirelog.objects.get(isGood = True,uid_id=uid,aid_id=good_id).delete() #,fid_id=-1
            return HttpResponse("aa")
#差评　isGood = False
def admire_badnum_views(request):
    if request.method == 'POST':    
        uid = request.POST.get('userID')
        bad_content = request.POST.get('badINPUT')
        bad_id = request.POST.get('badID')
        admireType = request.POST.get('admireType')
        isAdd = request.POST.get('isAdd')
        user = User.objects.get(username=request.session['username'])
        file=File.objects.get(id=bad_id)
        user1=User.objects.get(id=file.user_id)
        # 文件
        if admireType == 'file':  
            File.objects.filter(id=bad_id).update(file_benotadmired = bad_content)
            if isAdd=='1':
                Admirelog.objects.create(uid_id=uid,fid_id=bad_id,isGood=False,isFile=True)#,fid_id=-1
                n = Notification(aim_user=user1, arg0=4,arg4=user)
                n.save()
            else:
                Admirelog.objects.get(isGood=False,uid_id=uid,fid_id=bad_id).delete()#,fid_id=-1
            return HttpResponseRedirect('/share') 
        # 文章
        else:
            Article.objects.filter(id=bad_id).update(benotadmired_num=bad_content) 
            if isAdd=='1':
                Admirelog.objects.create(uid_id=uid,aid_id=bad_id,isGood=False,isFile=False)#,fid_id=-1
            else:
                Admirelog.objects.get(isGood=False,uid_id=uid,aid_id=bad_id).delete()#,fid_id=-1
            return HttpResponse("aa")
# uid fid aid isGood isFile create_time
# def check_name(request):
#     username = request.GET.get("username")
#     user=User.objects.get(username=username)
#     if(username == user.username):
#         str1 = "<font color='red'>username has been registered</font>"

#     else: 
#         str1 = "<font color='green'>username is available</font>"
#     return HttpResponse(json.dumps(str1))
#js中check
def check_name(request):
    username1 = request.GET.get("username")
    user=User.objects.filter(username=username1)
    print(user)
    if user:
        str1 = "<font color='red'>username has been registered</font>"
    elif username1=='':
        str1="<font color='red'>username can't be null</font>"
    else: 
        str1 = "<font color='green'>username is available</font>"
    return HttpResponse(json.dumps(str1))

def check_email(request):
    check_email=request.GET.get("email")
    user=User.objects.filter(email=check_email)
    if user:
        str1 = "<font color='red'>email has been registered</font>"
    elif check_email=='':
        str1="<font color='red'>email can't be null</font>"
    else: 
        str1 = "<font color='green'>email is available</font>"
    return HttpResponse(json.dumps(str1))
def check_name1(request):
    username1 = request.GET.get("username")
    user=User.objects.get(username=username1)
    if user:
        str1 = "<font color='green'>username is available</font>"
    elif username1=='':
        str1="<font color='red'>username can't be null</font>"
    else: 
        str1 = "<font color='red'>username not exist</font>"
        
    return HttpResponse(json.dumps(str1))

def check_pass(request):
    password1 = request.GET.get("password")
    username1 = request.GET.get("username")
    print(password1 + username1)
    user=User.objects.get(username=username1)
    print(user.email)
    if check_password(password1,user.password):
        str1 = "success"
    else: 
        str1 = "fail"
        
    return HttpResponse(json.dumps(str1))

def image_view(request):
    login_uname=request.session.get('username')
    user=User.objects.get(username=login_uname)
    request.session['login_from'] = request.META.get('HTTP_REFERER', '/')
    if request.method == 'POST':
        obj=request.FILES.get('image')
        file_path = os.path.join('static','upload','profile_photo',obj.name)
        f = open(file_path, 'wb')
        for chunk in obj.chunks():
            f.write(chunk)
        f.close()
        user.profile_photo=file_path
        user.save()
        return HttpResponseRedirect(request.session['login_from'])
    message.error("修改头像失败")
    return HttpResponseRedirect('/')
