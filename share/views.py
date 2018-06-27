from django.shortcuts import render
from django.http import HttpResponse
from django.http import FileResponse
from django.http import HttpResponseRedirect
from .models import *
from index.models import *
import os
from django.db.models import F
# Create your views here.
#show files
def show_files(request):
    files=File.objects.all();
    return render(request,'showfiles.html',locals())
#upload files
def upload_file(request):
    if request.method == 'GET':
        return render(request,'file.html')
    else:
        user_name = request.POST.get('user')
        classify = request.POST.get('list')
        user2=User.objects.get(username=user_name)
        file_classify=FileClassify.objects.get(title=classify)
        userid=user2.id
        classifyid= file_classify.id
        if userid != '' and classifyid!='':
            obj = request.FILES.get('inputfile')
            filetype=obj.name.split('.')[1]#获取后缀名
            if filetype!='':
                file_path = os.path.join('share','upload',obj.name)
                f = open(file_path, 'wb')
                for chunk in obj.chunks():
                    f.write(chunk)
                f.close()
                File.objects.create(file_name=obj.name,user_id=userid,file_size=obj.size,file_bedown=0,file=file_path,file_type=filetype,file_classify_id=classifyid)
                return HttpResponseRedirect('/show_file')
            return HttpResponse('上传文件类型错误')
        return HttpResponse('上传失败')
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
    return HttpResponseRedirect('/show_file')