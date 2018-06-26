from django.shortcuts import render
from django.http import HttpResponse

from .models import *
from index.models import *
import os
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
        user1 = request.POST.get('user')
        fafafa = request.POST.get('inputfile')
        classify1 = request.POST.get('list')
        if classify1 !=None:
            print(classify1)
        print(user1)

        user2=User.objects.get(username=user1)
        classify2=FileClassify.objects.get(title=classify1)
        userid=user2.id
        classifyid=classify2.id
        if userid != '':
            obj = request.FILES.get('inputfile')
            filetype=obj.name.split('.')[1]
            print(type1)
            file_path = os.path.join('share','upload',obj.name)
            print(file_path)

            f = open(file_path, 'wb')
            for chunk in obj.chunks():
                f.write(chunk)
            f.close()
            File.objects.create(fileName=obj.name,user_id=userid,fileSize=obj.size,fileBeDown=0,file=file_path,fileType=filetype,fileClassify_id=classifyid)
            return HttpResponse('上传成功')
        return HttpResponse('上传失败')
#download files
def bigFileView(request,a):
    def readFile(fn, buf_size=262144):
        f = open(fn, "rb")
        while True:
            c = f.read(buf_size)
            if c:
                yield c
            else:
                break
        f.close()
    file_name = "big_file.txt"
    response = HttpResponse(readFile(file_name))
    return response


#delete files