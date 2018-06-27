from django.shortcuts import render
from .models import *
from index.models import User

# Create your views here.
def index_views(request):
    if request.method == 'GET':

        return render(request,'market_index.html',locals())

def docs_views(request):
    if request.method == 'GET':
        return render(request,'docs_index.html',locals())
def goods_views(request):
    if request.method == 'GET':
        goods = Good.objects.all().order_by('create_time')
        print(goods[0].name)
        return render(request,'goods_index.html',locals())


#确认购买页面
def ordering_views(request, good_id):

    return render(request, 'ordering.html')
#支付页面
def paying_views(request, good_id):

    return render(request, 'paying.html')

def add_good_views(request):
    if request.method == 'GET':
        return render(request,'new_good.html',locals())
def good_detail_views(request,good_id):
    if request.method=='GET':
        return render(request,'good_detail.html',locals())