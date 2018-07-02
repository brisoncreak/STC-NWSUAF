from django.shortcuts import render, redirect, reverse
from .models import *
from index.models import User, Notification
from django.db.models import F,Q
from django.contrib import messages
from STC_NWSUAF.tools import login_required

from dwebsocket import require_websocket
from bs4 import BeautifulSoup

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
        page_now = request.GET.get('page')
        if not page_now:
            page_now = 1
        page_now = int(page_now)
        per_page = 4
        page_sum = len(goods)//per_page+1
        if page_sum > 6:
            page_sum = len(goods)//per_page
        else:
            page_sum = len(goods)//per_page+1
        start_page = (page_now-1)*per_page
        next_page = page_now + 1
        pre_page = page_now - 1
        goods = goods[start_page:start_page+per_page]
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
        confirm = request.POST.get('confirm-buy', '')
        if confirm == '':
            messages.warning(request, '你未确认交易信息')
            return render(request, 'ordering.html', locals())
        else:
            good = Good.objects.get(id=good_id)
            user = User.objects.get(username=request.session['username'])
            
            if good.creator == user:
                messages.warning(request, '不允许购买自己发布的商品')
                return render(request, 'ordering.html', locals())

            new_order = Order(status=0, creator=user, good=good)
            new_order.save()
            n = Notification(aim_user=good.creator, arg0=1, arg1=new_order.id, arg4=user)
            n.save()
            return redirect(reverse('paying', args=(new_order.id,)))

#支付页面
@login_required
def paying_views(request, order_id):
    if request.method == 'GET':
        user = User.objects.get(username=request.session['username'])
        order = Order.objects.get(id=order_id)
        good = order.good
        is_buyer = user == order.creator
        try:
            noti0 = Notification.objects.filter(Q(arg0=0)&Q(arg1=order_id)&Q(aim_user=user))
            for i in noti0:
                i.have_read = True
                i.arg2 = 0
                i.save()
            noti1 = Notification.objects.filter(Q(arg0=1)&Q(aim_user=user))
            for i in noti1:
                i.have_read = True
                i.save()
            noti2 = Notification.objects.filter(Q(arg0=2)&Q(aim_user=user))
            for i in noti2:
                i.have_read = True
                i.save()
            noti3 = Notification.objects.filter(Q(arg0=3)&Q(aim_user=user))
            for i in noti3:
                i.have_read = True
                i.save()
        except:
            print('bucunzai')
            
        readt = TradeMessage.objects.filter(Q(order=order)&Q(receiver=user))
        for t in readt:
            t.have_read = True
            t.save()

        tmessages = TradeMessage.objects.filter(order=order).order_by('create_time')
        
        return render(request, 'paying.html', locals())
    return redirect('/')


#创建新商品页面
@login_required
def add_good_views(request):
    if request.method == 'GET':
        return render(request,'new_good.html',locals())

def order_views(request,orderstate):
    if request.method == 'GET':
        order_list = Order.objects.all().order_by('-create_time')
        #good = order_list.good__set.all()
        return render(request,'order_view.html',locals())
def order_finished_views(request,orderstate):
    if request.method == 'GET':
        return render(request,'order_finish.html',locals())
def order_complaint_views(request,orderstate):
    if request.method == 'GET':
        return render(request,'order_complaint.html',locals())
def order_cancel_views(request,orderstate):
    if request.method == 'GET':
        return render(request,'order_cancel.html',locals())
def order_detail_views(request,goodname):
    if request.method == 'GET':
        return render(request,'order_detail.html',locals())
def complaint_views(request,orderid):
    if request.method == 'GET':
        return render(request,'complaint.html',locals())
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
                try:
                    n = Notification.objects.get(Q(arg0=0)&Q(arg1=order_id)&Q(aim_user=seller))
                    n.arg2 += 1
                    n.have_read = False
                except:
                    n = Notification(aim_user=seller, arg0=0, arg1=order_id, arg2=1, arg3=0, arg4=user)
            else:
                message = TradeMessage(sender=user, receiver=buyer, order=order, content=content)
                try:
                    n = Notification.objects.get(Q(arg0=0)&Q(arg1=order_id)&Q(aim_user=buyer))
                    n.arg2 += 1
                    n.have_read = False
                except:
                    n = Notification(aim_user=buyer, arg0=0, arg1=order_id, arg2=1, arg3=1, arg4=user)
                    #arg0:0聊天信息 1交易信息 2买家已付款 3卖家已确认
                    #arg1:订单id 
                    #arg2:暂存消息数量吧
                    #arg3:0由买家发来 1由卖家发来
                    #arg4:用户外键
            message.save()
            n.save()

        return render(request, 'paying.html', locals())

#买家确认
@login_required
def buyer_ok_views(request, order_id):
    if request.method == 'POST': 
        user = User.objects.get(username=request.session['username'])
        order = Order.objects.get(id=order_id)

        if user != order.creator:
            messages.error(request, '没有权限')
            return render(request, '/', locals())
        order.buyer_ok = True
        order.status = 1
        order.save()

        #消息处理
        good = order.good
        buyer = order.creator
        seller = good.creator

        buyer_message = request.POST.get('buyer-ok-message', '')
        
        if not buyer_message == '':
            message = TradeMessage(sender=user, receiver=seller, order=order, content=buyer_message)
            n = Notification(aim_user=seller, arg0=2, arg1=order_id, arg4=user)
            
            message.save()
            n.save()


        return redirect(reverse('paying', args=(order.id,)))


@login_required
def seller_ok_views(request, order_id):
    if request.method == 'POST': 
        user = User.objects.get(username=request.session['username'])
        order = Order.objects.get(id=order_id)
        if user != order.good.creator:
            messages.error(request, '没有权限')
            return render(request, '/', locals())

        order.buyer_ok = True
        order.status = 2
        order.save()
        
        good = order.good
        good.sell_times += 1
        good.save()
            
        buyer = order.creator
        buyer.trade_count += 1
        buyer.save()

        seller = good.creator
        seller.trade_count += 1
        seller.save()


        #消息处理
        n = Notification(aim_user=buyer, arg0=3, arg1=order_id, arg4=user)
        n.save()

        return redirect(reverse('paying', args=(order.id,)))

@require_websocket
def market_ws_views(request, order_id, uid):
    for message in request.websocket:
        if message == b'456':
            #request.websocket.send(b'456')
            #print(message)
            user = User.objects.get(id=uid)
            order = Order.objects.get(id=order_id)
            good = order.good
            is_buyer = user == order.creator
            tmessages = TradeMessage.objects.filter(order=order).order_by('create_time')

            readt = TradeMessage.objects.filter(Q(order=order)&Q(receiver=user))
            for t in readt:
                t.have_read = True
                t.save()
            
            html = render(request, 'paying.html', locals()).content
            bs = BeautifulSoup(html, "html.parser")
            noti_div = bs.find('div', id='paycontent').find('div', id='fresh_area')

            request.websocket.send(noti_div.encode('utf-8'))
