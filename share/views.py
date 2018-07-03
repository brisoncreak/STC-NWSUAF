from django.shortcuts import render
from django.http import HttpResponse
from django.http import FileResponse
from django.http import HttpResponseRedirect
from .models import *
from index.models import *
from index.templates import *
import os
from django.db.models import F
from django.contrib import messages
from STC_NWSUAF.tools import login_required
from urllib.parse import unquote

# Create your views here.


#upload files
def upload_file(request):
    if request.method == 'GET':
        colleges = Colleges.objects.all()
        return render(request,'file.html',locals())
    else:
        classify = request.POST.get('list')      
        file_classify=Colleges.objects.get(title=classify)      
        classifyid= file_classify.id
        if request.session.get('username'):
            user_name=request.session.get('username')
            user2=User.objects.get(username=user_name)
            userid=user2.id
            if userid != '' and classifyid!='':
                obj = request.FILES.get('inputfile')
                file_path = os.path.join('share','upload',obj.name)
                f = open(file_path, 'wb')
                for chunk in obj.chunks():
                    f.write(chunk)
                f.close()
                File.objects.create(file_name=obj.name,user_id=userid,file_size=obj.size,file_bedown=0,file=file_path,file_classify_id=classifyid)
                messages.success(request,'上传成功')
                return HttpResponseRedirect('/share')
            messages.error(request,'上传失败')
            return HttpResponseRedirect('/upload_file')
        messages.error(request,'请登录')
        return HttpResponseRedirect('/login')

#upload files
def upload_file2(request,collegename):
    name = unquote(collegename, 'utf-8')

    if request.method == 'GET':
        return render(request,'singleCollegeUpload.html',locals())
    else:
        file_classify=Colleges.objects.get(title=name)           
        classifyid= file_classify.id
        if request.session.get('username'):
            user_name=request.session.get('username')
            user2=User.objects.get(username=user_name)
            userid=user2.id
            if userid != '' and classifyid!='':
                obj = request.FILES.get('inputfile')
                file_path = os.path.join('share','upload',obj.name)
                file=File.objects.filter(file_name=obj.name)
                if file!='':
                    repeat_name=obj.name
                    print(repeat_name)
                    i=0
                    file1=File.objects.filter(file_name=repeat_name)
                    while True:
                        repeat_divi =str(i)+'-'
                        repeat_name = repeat_divi + obj.name
                        i += 1
                        file1=File.objects.filter(file_name=repeat_name)
                        if file1.count()==0:

                            break
                    messages.warning(request,'您上传的文件已存在，已为您重新命名')
                    filename=repeat_name
                else:
                    filename=obj.name

                file_path = os.path.join('share','upload',filename)
                f = open(file_path, 'wb')
                for chunk in obj.chunks():
                    f.write(chunk)
                f.close()
                File.objects.create(file_name=filename,user_id=userid,file_size=obj.size,file_bedown=0,file=file_path,file_classify_id=classifyid)
                
                messages.success(request,'上传成功')
                # return HttpResponseRedirect('/share')
                return HttpResponseRedirect('/show_College/'+collegename)
                #return render(request,'singleCollegeShow.html',locals())   # /upload_file2/collegename

            messages.error(request,'上传失败')
            return HttpResponseRedirect('/upload_file')
        messages.error(request,'请登录')
        return HttpResponseRedirect('/login')

		
#download files
def download_files(request,fileid):  
    file=File.objects.get(id=fileid)
    file_name = file.file_name
    File.objects.filter(id=fileid).update(file_bedown=F('file_bedown')+1)
    file_path = os.path.join('share','upload',file_name) 
    file=open(file_path,'rb')  
    response =FileResponse(file)  
    response['Content-Type']='application/octet-stream'  
    response['Content-Disposition']='attachment;filename='+file_name  
    return response
#delete files
def delete_files(request,fileid):
    file=File.objects.get(id=fileid)
    File.objects.get(id=fileid).delete()   
    file_name=file.file_name
    file_path = os.path.join('share','upload',file_name)
    if os.path.isfile(file_path):
        os.remove(file_path)
    return HttpResponseRedirect('/share')
@login_required
#show files
def index_views(request):
    sharefileList = File.objects.all()
    colleges = Colleges.objects.all()
    collegetypes = Collegetype.objects.all()
    #1
    wenketype = Collegetype.objects.get(title='文科')
    wenkecolleges = Colleges.objects.filter(classify_id=wenketype.id)
    wenkes = []
    for wenke in wenkecolleges:
        wenkes.append(wenke.title)
    #2
    liketype = Collegetype.objects.get(title='理科')
    likecolleges = Colleges.objects.filter(classify_id=liketype.id)
    likes = []
    for like in likecolleges:
        likes.append(like.title)
    #3
    gongketype = Collegetype.objects.get(title='工科')
    gongkecolleges = Colleges.objects.filter(classify_id=gongketype.id)
    gongkes = []
    for gongke in gongkecolleges:
        gongkes.append(gongke.title)

    #4
    nongketype = Collegetype.objects.get(title='农科')
    nongkecolleges = Colleges.objects.filter(classify_id=nongketype.id)   #得到了querySet集合
    # print(nongkecolleges)
    #转化为列表
    nongkes = []
    for nongke in nongkecolleges:
        nongkes.append(nongke.title)
    # print(nongkes)

    if request.method == 'GET':
        return render(request,'share_index.html',locals()) 
    else:
        collegetitle = request.POST.get('selcollege')  
        return HttpResponseRedirect('/show_College/'+collegetitle)



def show_college(request,collegetitle):
    college = Colleges.objects.get(title=collegetitle)
    files = File.objects.filter(file_classify_id=college.id)
    return render(request,'singleCollegeShow.html',locals()) 

def show_user(request,userid):
    user = User.objects.get(id=userid)
    listfile = File.objects.filter(user_id=userid).order_by("-id")
    return render(request,'userFilesShow.html',locals())

def show_file(request,fileid):
    file = File.objects.get(id=fileid)
    return render(request,'fileDetailShow.html',locals())

def admire_views(request):
    return render(request,'admire.html',locals())