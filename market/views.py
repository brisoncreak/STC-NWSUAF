from django.shortcuts import render, redirect, reverse
from .models import *
from index.models import User

from django.contrib import messages
from STC_NWSUAF.tools import login_required

# Create your views here.

def index_views(request):
    if request.method == 'GET':

        return redirect(reverse('goods_index'))
#付费文档页面
def docs_views(request):
    if request.method == 'GET':
        return render(request,'docs_index.html',locals())
#二手商品页面

def goods_views(request):
    if request.method == 'GET':
        goods = Good.objects.all().order_by('-create_time')
        return render(request,'goods_index.html',locals())
#商品详情页面
def good_detail_views(request,good_id):
    if request.method=='GET':
        good = Good.objects.get(id=good_id)
        return render(request,'good_detail.html',locals())

#确认购买页面
@login_required
def ordering_views(request, good_id):
    good = Good.objects.get(id=good_id)
    return render(request, 'ordering.html', locals())
#创建订单视图
@login_required
def new_order_views(request, good_id):
    if request.method == 'POST':
        good = Good.objects.get(id=good_id)
        user = User.objects.get(username=request.session['username'])
        new_order = Order(status=0, creator=user, good=good)
        new_order.save()
        return redirect(reverse('paying', args=(new_order.id,)))

#支付页面
@login_required
def paying_views(request, order_id):
    if request.method == 'GET':
        order = Order.objects.get(id=order_id)
        good = order.good

        tmessages = TradeMessage.objects.filter(order=order).order_by('create_time')
        return render(request, 'paying.html', locals())
    return redirect('/')


#创建新商品页面
@login_required
def add_good_views(request):
    if request.method == 'GET':
        return render(request,'new_good.html', locals())

def add_tmessage_views(request, order_id):
    if request.method == 'POST':
        content = request.POST.get('content', '')
        order = Order.objects.get(id=order_id)
        good = order.good
        user = User.objects.get(username=request.session['username'])
        buyer = order.creator
        seller = good.creator
        if not content == '':
            if user.id == buyer.id:
                message = TradeMessage(sender=user, receiver=seller, order=order, content=content)
            else:
                message = TradeMessage(sender=user, receiver=buyer, order=order, content=content)

            message.save()

        messages.success(request,'已发送')
        return render(request, 'paying.html', locals())

