from django.shortcuts import render

# Create your views here.
def market_views(request):
    if request.method == 'GET':
        return render(request,'market.html',locals())