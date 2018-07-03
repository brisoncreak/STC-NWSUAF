from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import *
from django.views.decorators.csrf import csrf_exempt,csrf_protect
from django.db.models import Q
from django.contrib import messages

from STC_NWSUAF.tools import login_required


# Create your views here.
def index_views(request):
    
    listArticle=Article.objects.all().order_by("-id")

    return render(request,'query_article.html',locals())

@login_required
def query_article_views(request):
    
    if request.session.get('id'):
        uid=request.session.get('id')
    listArticle=Article.objects.all().order_by("-id")

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
    listCollegetype=Collegetype.objects.all().order_by("-id")
    if request.method == 'GET':
        return render(request,'add_article.html',locals())
    else:
        atopic=request.POST.get('topic')
        alable=request.POST.get('lable')
        acontent=request.POST.get('content')
        acollegetype_id=request.POST.get('collegetype_id')
        ais_reviewed=request.POST.get('is_reviewed')
        if ais_reviewed=="on":
            ais_reviewed=1
        else:
            ais_reviewed=0

        if request.session.get('username'):
            uname=request.session.get('username')
            u=User.objects.get(username=uname)
         
            Article.objects.create(topic=atopic,lable=alable,content=acontent,is_reviewed=ais_reviewed,reviewed_num=0,skim_num=0,like_num=0,collegetype_id=acollegetype_id,user_id=u.id)            
            # b=Block.objects.get(id=ablock_id)
            # b.article_num=b.article_num+1
            # b.save() 
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

