from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse
from django.http import FileResponse
from django.http import HttpResponseRedirect
from .models import *
from index.models import *
from chat.models import *
from index.templates import *
import os
from django.db.models import F
from django.contrib import messages
from STC_NWSUAF.tools import login_required
from urllib.parse import unquote

# Create your views here.


#upload files
def upload_file(request):
    login_uname=request.session.get('username')
    user=User.objects.get(username=login_uname)
    if request.method == 'GET':
        colleges = Colleges.objects.all()
        return render(request,'file.html',locals())
    else:
        #获取文件的状态名和对应的编号
        # 状态   0代表私有文档　　１代表免费共享文档　　　２　代表付费共享文档
        status_name = request.POST.get('fileStaus')  #文件的状态
        if status_name == '私有文档':
            status = 0
        elif status_name=='免费共享文档':
            status = 1
        else:
            status = 2
        classify = request.POST.get('list')    #属于的学院
        file_classify=Colleges.objects.get(title=classify) 
        classifyid= file_classify.id#学院的id
        if request.session.get('username'):
            user_name=request.session.get('username')
            user2=User.objects.get(username=user_name)
            userid=user2.id
            #登录且有学院信息　　此时要保存
            if userid != '' and classifyid!='': 
                obj = request.FILES.get('inputfile')
                samename_files=File.objects.filter(file_name=obj.name)
                print(samename_files)
                if samename_files.count()!=0:
                    repeat_name=obj.name
                    i=0
                    while True:
                        repeat_divi =str(i)+'-'
                        repeat_name = repeat_divi + obj.name
                        i += 1
                        file1=File.objects.filter(file_name=repeat_name)
                        if file1.count()==0:
                            break
                    messages.warning(request,'您上传的文件已存在，已为您重新命名')
                    filename=repeat_name
                #如果没有的文件
                else:
                    filename=obj.name

                #写文件
                file_path = os.path.join('share','upload',filename)
                f = open(file_path, 'wb')
                for chunk in obj.chunks():
                    f.write(chunk)
                f.close()

                File.objects.create(file_name=filename,user_id=userid,file_size=obj.size,file_bedown=0,file=file_path,file_status=status,file_classify_id=classifyid,file_beadmired=0,file_benotadmired=0)
                if status==1 or status==0:
                    messages.success(request,'上传成功')
                    return HttpResponseRedirect('/share')
                elif status==2:
                    messages.success(request,'请完善商品信息')
                    file = File.objects.get(file_name = filename)
                    return redirect('/market/add_good/'+str(file.id))
            messages.error(request,'上传失败')
            return HttpResponseRedirect('/upload_file')
        messages.error(request,'请登录')
        return HttpResponseRedirect('/login')

#upload files
def upload_file2(request,collegename):
    login_uname=request.session.get('username')
    user=User.objects.get(username=login_uname)
    name = unquote(collegename, 'utf-8')
    #上传文件
    if request.method == 'GET':
        return render(request,'singleCollegeUpload.html',locals())
    #上传完成　　保存文件　　其中涉及到的重命名
    else:
        #获得文件的状态
        status_name = request.POST.get('fileStaus')  
        if status_name == '私有文档':
            status = 0
        elif status_name=='免费共享文档':
            status = 1
        else:
            status = 2
        # 得到文件所属的学院以及学院的id
        file_classify=Colleges.objects.get(title=name)
        classifyid= file_classify.id 
        #判断是否登录
        if request.session.get('username'):
            user_name=request.session.get('username')
            user2=User.objects.get(username=user_name)
            userid=user2.id

            #登录且有学院信息　　此时要保存
            if userid != '' and classifyid!='':
                #得到上传的文件的存放路径
                obj = request.FILES.get('inputfile')   
                samename_files=File.objects.filter(file_name=obj.name)
                #如果有重名的文件
                if samename_files.count()!=0:
                    repeat_name=obj.name
                    i=0
                    while True:
                        repeat_divi =str(i)+'-'
                        repeat_name = repeat_divi + obj.name
                        i += 1
                        file1=File.objects.filter(file_name=repeat_name)
                        if file1.count()==0:
                            break
                    messages.warning(request,'您上传的文件已存在，已为您重新命名')
                    filename=repeat_name
                #如果没有的文件
                else:
                    filename=obj.name
                #设置重命名成功后的存放路径
                file_path = os.path.join('share','upload',filename)
                f = open(file_path, 'wb')
                for chunk in obj.chunks():
                    f.write(chunk)
                f.close()
                File.objects.create(file_name=filename,user_id=userid,file_size=obj.size,file_bedown=0,file=file_path,file_status=status,file_classify_id=classifyid,file_beadmired=0,file_benotadmired=0)
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
    File.objects.filter(id=fileid).update(file_bedown=F('file_bedown')+1) #更改被下载次数
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


#show files
def index_views(request):
    sharefileList = File.objects.all().exclude(file_status=0)

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

    login_uname=request.session.get('username')
    user=User.objects.get(username=login_uname)
    login_uid=user.id

    #用于使显示打赞和数据库中的赞表同步
    # 获取了对应登录用户　　对文件好评的相应文件列表
    listfile_admireQ = Admirelog.objects.filter(uid_id=login_uid).filter(isGood = 1).filter(isFile = 1).values('fid_id')
    listfile_admire = []
    for i in listfile_admireQ:
        listfile_admire.append(i['fid_id'])
    # 获取了对应登录用户　　对文件差评的相应文件列表
    listfile_notadmireQ = Admirelog.objects.filter(uid_id=login_uid).filter(isGood = 0).filter(isFile = 1).values('fid_id')
    listfile_notadmire = []
    for j in listfile_notadmireQ:
        listfile_notadmire.append(j['fid_id'])

    if request.method == 'GET':
        page_now = request.GET.get('page')
        if not page_now:
            page_now = 1
        page_now = int(page_now)
        per_page = 14
        page_sum = len(sharefileList)//per_page+1
        if page_sum > 6:
            page_sum = len(sharefileList)//per_page
        else:
            page_sum = len(sharefileList)//per_page+1
        start_page = (page_now-1)*per_page
        next_page = page_now + 1
        pre_page = page_now - 1
        sharefileList = sharefileList[start_page:start_page+per_page]
        show_sum = page_sum//6+1 
        lis = []
        for i in range(1,show_sum+1):
            lis.append(i)
        for i in lis:
            if page_now in range(i*6-5,i*6+1):
                    ranges = range(i*6-5,i*6+1)
        if page_sum in ranges:
                    ranges = range(i*6-5,page_sum+1)
        print(page_sum)
        return render(request,'share_index.html',locals()) 
    else:
        collegetitle = request.POST.get('selcollege')  
        return HttpResponseRedirect('/show_College/'+collegetitle)


#按照学院显示文件
def show_college(request,collegetitle):
    login_uname=request.session.get('username')
    user=User.objects.get(username=login_uname)
    college = Colleges.objects.get(title=collegetitle)
    files = File.objects.filter(file_classify_id=college.id)
    page_now = request.GET.get('page')
    if not page_now:
        page_now = 1
    page_now = int(page_now)
    per_page = 14
    page_sum = len(files)//per_page+1
    if page_sum > 6:
        page_sum = len(files)//per_page
    else:
        page_sum = len(files)//per_page+1
    start_page = (page_now-1)*per_page
    next_page = page_now + 1
    pre_page = page_now - 1
    files = files[start_page:start_page+per_page]
    show_sum = page_sum//6+1 
    lis = []
    for i in range(1,show_sum+1):
        lis.append(i)
    for i in lis:
        if page_now in range(i*6-5,i*6+1):
                ranges = range(i*6-5,i*6+1)
    if page_sum in ranges:
                ranges = range(i*6-5,page_sum+1)
    print(page_sum)
    return render(request,'singleCollegeShow.html',locals()) 
#按照用户显示文件
def show_user(request,userid):
    login_uname=request.session.get('username')
    user=User.objects.get(username=login_uname)
    login_uid=user.id

    # print(login_uid)
    # print("**********88")
    # print(type(userid))
    user1 = User.objects.get(id=userid)
    #看自己的文件　　就不需要得到赞表
    if int(userid) == login_uid:
        listfile = File.objects.filter(user_id=userid).order_by("-id")
        page_now = request.GET.get('page')
        if not page_now:
            page_now = 1
        page_now = int(page_now)
        per_page = 14
        page_sum = len(listfile)//per_page+1
        if page_sum > 6:
            page_sum = len(listfile)//per_page
        else:
            page_sum = len(listfile)//per_page+1
        start_page = (page_now-1)*per_page
        next_page = page_now + 1
        pre_page = page_now - 1
        listfile = listfile[start_page:start_page+per_page]
        show_sum = page_sum//6+1 
        lis = []
        for i in range(1,show_sum+1):
            lis.append(i)
        for i in lis:
            if page_now in range(i*6-5,i*6+1):
                    ranges = range(i*6-5,i*6+1)
        if page_sum in ranges:
                    ranges = range(i*6-5,page_sum+1)
        print(page_sum)
        return render(request,'userFilesShow.html',locals())
    #看其他人的文件　　需要得到赞表
    else:
        listfile = File.objects.filter(user_id=userid).exclude(file_status=0).order_by("-id")


        # 获取了对应登录用户　　对文件好评的相应文件列表
        listfile_admireQ = Admirelog.objects.filter(uid_id=login_uid).filter(isGood = 1).filter(isFile = 1).values('fid_id')
        listfile_admire = []
        for i in listfile_admireQ:
            listfile_admire.append(i['fid_id'])
        # 获取了对应登录用户　　对文件差评的相应文件列表
        listfile_notadmireQ = Admirelog.objects.filter(uid_id=login_uid).filter(isGood = 0).filter(isFile = 1).values('fid_id')
        listfile_notadmire = []
        for j in listfile_notadmireQ:
            listfile_notadmire.append(j['fid_id'])
        page_now = request.GET.get('page')
        if not page_now:
            page_now = 1
        page_now = int(page_now)
        per_page = 14
        page_sum = len(listfile)//per_page+1
        if page_sum > 6:
            page_sum = len(listfile)//per_page
        else:
            page_sum = len(listfile)//per_page+1
        start_page = (page_now-1)*per_page
        next_page = page_now + 1
        pre_page = page_now - 1
        listfile = listfile[start_page:start_page+per_page]
        show_sum = page_sum//6+1 
        lis = []
        for i in range(1,show_sum+1):
            lis.append(i)
        for i in lis:
            if page_now in range(i*6-5,i*6+1):
                    ranges = range(i*6-5,i*6+1)
        if page_sum in ranges:
                    ranges = range(i*6-5,page_sum+1)
        print(page_sum)
        return render(request,'otherUserFilesShow.html',locals())

#商品详情
def show_file(request,fileid):
    file = File.objects.get(id=fileid)
    login_uname=request.session.get('username')
    user=User.objects.get(username=login_uname)
    return render(request,'fileDetailShow.html',locals())



#包括article中的方法    已经写到了ｉｎｄｅｘ应用中

# from django.views.decorators.csrf import csrf_exempt
# @csrf_exempt
# def admire_goodnum_views(request):
#     if request.method == 'POST':
#         good_content = request.POST.get('goodINPUT')
#         good_id = request.POST.get('goodID')
#         admireType = request.POST.get('admireType')
#     print(admireType)
#     if admireType == 'file':
#         File.objects.filter(id=good_id).update(file_beadmired = good_content)
#     else:
#         Article.objects.filter(id=good_id).update(beadmired_num=good_content)
        

# def admire_badnum_views(request):
#     if request.method == 'POST':      
#         bad_content = request.POST.get('badINPUT')
#         bad_id = request.POST.get('badID')
#         admireType = request.POST.get('admireType')
#     print(admireType)
#     if admireType == 'file':  
#         File.objects.filter(id=bad_id).update(file_benotadmired = bad_content)
#     else:
#         Article.objects.filter(id=bad_id).update(benotadmired_num=bad_content) 
