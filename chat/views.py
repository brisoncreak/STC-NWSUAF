from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import *
from index.models import Admirelog
from django.views.decorators.csrf import csrf_exempt,csrf_protect
from django.db.models import Q
from django.contrib import messages

from STC_NWSUAF.tools import login_required


# 游客访问
def index_views(request):
    if request.method == 'GET':
        listArticle=Article.objects.all().order_by("-id")
        page_now = request.GET.get('page')
        if not page_now:
            page_now = 1
        page_now = int(page_now)
        per_page = 5
        page_sum = len(listArticle)//per_page+1
        if page_sum > 6:
            page_sum = len(listArticle)//per_page
        else:
            page_sum = len(listArticle)//per_page+1
        start_page = (page_now-1)*per_page
        next_page = page_now + 1
        pre_page = page_now - 1
        listArticle = listArticle[start_page:start_page+per_page]
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

        return render(request,'query_article.html',locals())


#　登录用户访问
@login_required
def query_article_views(request):
    
    if request.session.get('id'):
        uid=request.session.get('id')
    listArticle=Article.objects.all().order_by("-id")
    page_now = request.GET.get('page')
    if not page_now:
        page_now = 1
    page_now = int(page_now)
    per_page = 5
    page_sum = len(listArticle)//per_page+1
    if page_sum > 6:
        page_sum = len(listArticle)//per_page
    else:
        page_sum = len(listArticle)//per_page+1
    start_page = (page_now-1)*per_page
    next_page = page_now + 1
    pre_page = page_now - 1
    listArticle = listArticle[start_page:start_page+per_page]
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

    return render(request,'query_article.html',locals())

def read_my_views(request):
    if request.session.get('username'):
        uname=request.session.get('username')
        u=User.objects.get(username=uname)

        listArticle=Article.objects.filter(user_id=u.id).order_by("-id")

        for article in listArticle:
            listReviews=[]
            reviews = Review.objects.filter(article_id=article.id).order_by("-id")
            for review in reviews:
               
                uname=User.objects.get(id=review.user_id)
                usercomment=str(uname)+"|"+review.content+"|"+str(review.create_date)
   
                listReviews.append(usercomment)
            Article.objects.filter(id=article.id).update(reviews=listReviews)

        page_now = request.GET.get('page')
        if not page_now:
            page_now = 1
        page_now = int(page_now)
        per_page = 3
        page_sum = len(listArticle)//per_page+1
        if page_sum > 6:
            page_sum = len(listArticle)//per_page
        else:
            page_sum = len(listArticle)//per_page+1
        start_page = (page_now-1)*per_page
        next_page = page_now + 1
        pre_page = page_now - 1
        listArticle = listArticle[start_page:start_page+per_page]
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

        return render(request,'read_my.html',locals())
    else:
        messages.error(request,'请登录!')
        return HttpResponseRedirect('/')

def read_sb_views(request,id):
    u=User.objects.get(id=id)
    listArticle=Article.objects.filter(user_id=id).order_by("-id")
    return render(request,'read_sb.html',locals())

def read_article_views(request,id):

    a=Article.objects.get(id=id)
    listReview=Review.objects.filter(article_id=a.id).order_by("-id")
    for review in listReview:
        listReplys=[]
        replys=Reply.objects.filter(review_id=review.id).order_by("-id")
        for reply in replys:
            uname=User.objects.get(id=reply.user_id)
            userreply=[str(uname)+"|"+reply.content+"|"+str(reply.create_date)]
            
            listReplys.append(userreply)
        Review.objects.filter(id=review.id).update(replys=listReplys)


    return render(request,'read_article.html',locals())

def del_article_views(request,id):
    Article.objects.get(id=id).delete()
    messages.success(request,'文章删除成功！')
    return HttpResponseRedirect('/read_my')                                                                    


def del_review_views(request,id,uid,aid):
    Review.objects.filter(Q(user_id=uid)|Q(article_id=aid)).get(id=id).delete()
    return HttpResponse("评论删除成功！")

@csrf_exempt
@login_required
def add_article_views(request): 
    # listCollegetype=Collegetype.objects.all().order_by("-id")

    # 获取所有的学院类型已经其下的所有学院　级联下拉框###########################
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

# 获取所有的学院类型已经其下的所有学院　级联下拉框###########################



    if request.method == 'GET':
        return render(request,'add_article.html',locals())
    else:
        atopic=request.POST.get('topic')
        alable=request.POST.get('lable')
        acontent=request.POST.get('content')
        acollegetype = request.POST.get('acollegetype')
        acollegetype_id = Collegetype.objects.get(title=acollegetype).id
        acollege = request.POST.get('acollege')
        acollege_id = Colleges.objects.get(title=acollege).id


        # acollegetype_id=request.POST.get('collegetype_id')
           
        ais_reviewed=request.POST.get('is_reviewed')
        if ais_reviewed=="on":
            ais_reviewed=1
        else:
            ais_reviewed=0

        if request.session.get('username'):
            uname=request.session.get('username')
            u=User.objects.get(username=uname)
         
            Article.objects.create(topic=atopic,lable=alable,content=acontent,is_reviewed=ais_reviewed,reviewed_num=0,skim_num=0,like_num=0,collegetype_id=acollegetype_id,college_id=acollege_id,user_id=u.id)            
            messages.success(request,'文章发布成功！')
            return HttpResponseRedirect('/chat/')
        else:
            messages.error(request,'请登录!')
            return HttpResponseRedirect('/')
 

@csrf_exempt
@login_required
def add_review_views(request,aid):
    if request.session.get('username'):
        uname=request.session.get('username')
        u=User.objects.get(username=uname)
        a=Article.objects.get(id=aid) 

        if request.method=='POST':      
            # 判断文章是否可被评论 
            if (a.is_reviewed=="1"):
                rcontent=request.POST.get('content')
                Review.objects.create(content=rcontent,article_id=aid,user_id=u.id)      
                a.reviewed_num=a.reviewed_num+1
                a.save()
                messages.success(request,'评论发布成功！')
                return HttpResponseRedirect('/read_article/'+str(a.id))
            else:
                messages.error(request,'文章不可被评论!')
                return HttpResponseRedirect('/read_article/'+str(a.id))
        else:
            return render(request,'add_review.html',locals())
    else:
        messages.error(request,'请登录!')
        return HttpResponseRedirect('/')

@csrf_exempt
@login_required
def add_reply_views(request,rid):
    if request.session.get('username'):
        uname=request.session.get('username')
        u=User.objects.get(username=uname)
        r=Review.objects.get(id=rid) 
        if request.method=='GET':
            return render(request,'add_reply.html',locals())
        else:
            rcontent=request.POST.get('content')
            Reply.objects.create(content=rcontent,review_id=rid,user_id=u.id)            
            messages.success(request,'回复评论成功！')

            return HttpResponseRedirect('/read_article/'+str(r.article_id))
    else:
        messages.error(request,'请登录!')
        return HttpResponseRedirect('/')

# def add_like_views(request,uid,aid):
#     u=User.objects.get(id=uid)
#     a=Article.objects.get(id=aid) 


import os
import time
import json
def file_manager(request):
    dic = {}
    root_path = '/home/tarena/Myproject/STC/static/'
    static_root_path = '/static/'
    request_path = request.GET.get('path')
    if request_path:
        abs_current_dir_path = os.path.join(root_path, request_path)
        move_up_dir_path = os.path.dirname(request_path.rstrip('/'))
        dic['moveup_dir_path'] = move_up_dir_path + '/' if move_up_dir_path else move_up_dir_path

    else:
        abs_current_dir_path = root_path
        dic['moveup_dir_path'] = ''

    dic['current_dir_path'] = request_path
    dic['current_url'] = os.path.join(static_root_path, request_path)

    file_list = []
    for item in os.listdir(abs_current_dir_path):
        abs_item_path = os.path.join(abs_current_dir_path, item)
        a, exts = os.path.splitext(item)
        is_dir = os.path.isdir(abs_item_path)
        if is_dir:
            temp = {
                'is_dir': True,
                'has_file': True,
                'filesize': 0,
                'dir_path': '',
                'is_photo': False,
                'filetype': '',
                'filename': item,
                'datetime': time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(os.path.getctime(abs_item_path)))
            }
        else:
            temp = {
                'is_dir': False,
                'has_file': False,
                'filesize': os.stat(abs_item_path).st_size,
                'dir_path': '',
                'is_photo': True if exts.lower() in ['.jpg', '.png', '.jpeg'] else False,
                'filetype': exts.lower().strip('.'),
                'filename': item,
                'datetime': time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(os.path.getctime(abs_item_path)))
            }

        file_list.append(temp)
    dic['file_list'] = file_list
    return HttpResponse(json.dumps(dic))

