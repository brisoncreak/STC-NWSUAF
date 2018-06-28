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
# Create your views here.
#show files
def show_files(request):
    files=File.objects.all();
    return render(request,'showfiles.html',locals())
#upload files
def upload_file(request):
    if request.method == 'GET':
        colleges = Colleges.objects.all()
        return render(request,'file.html',locals())
    else:
        user_name = request.POST.get('user')
        # print(user_name)
        classify = request.POST.get('list')
        print(classify)
        user2=User.objects.get(username=user_name)
        file_classify=Colleges.objects.get(title=classify)
        userid=user2.id
        classifyid= file_classify.id
        if userid != '' and classifyid!='':
            obj = request.FILES.get('inputfile')
            file_path = os.path.join('share','upload',obj.name)
            
            f = open(file_path, 'wb')
            for chunk in obj.chunks():
                f.write(chunk)
            f.close()
            File.objects.create(file_name=obj.name,user_id=userid,file_size=obj.size,file_bedown=0,file=file_path,file_classify_id=classifyid)
            # return HttpResponse('上传成功')
            messages.success(request,'上传成功')
            return HttpResponseRedirect('/share')
        messages.error(request,'上传失败')
        return HttpResponseRedirect('/upload_file')
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

def index_views(request):
    sharefileList = File.objects.all()
    colleges = Colleges.objects.all()

    collegetypes = Collegetype.objects.all()

    # wenketype = Collegetype.objects.filter(title='文科')
    # wenkecolleges = Colleges.objects.filter(classify_id=wenketype.id)


    # liketype = Collegetype.objects.filter(title='理科')
    # likecolleges = Colleges.objects.filter(classify_id=liketype.id)

    # gongketype = Collegetype.objects.filter(title='工科')
    # gongkecolleges = Colleges.objects.filter(classify_id=gongketype.id)

    # nongketype = Collegetype.objects.filter(title='农科')
    # nongkecolleges = Colleges.objects.filter(classify_id=nongketype.id)

    return render(request,'share_index.html',locals()) 

