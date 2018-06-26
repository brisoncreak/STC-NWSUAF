from django.shortcuts import render

from index.models import User

# Create your views here.
def index_views(request):
    return render(request,'market_index.html')

#确认购买页面
def ordering_views(request, good_id):

    return render(request, 'ordering.html')
#支付页面
def paying_views(request, good_id):

    return render(request, 'paying.html')
