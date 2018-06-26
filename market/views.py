from django.shortcuts import render

# Create your views here.
def index_views(request):
    if request.method == 'GET':
        return render(request,'market_index.html',locals())

def docs_views(request):
    if request.method == 'GET':
        return render(request,'docs_index.html',locals())
def goods_views(request):
    if request.method == 'GET':
        return render(request,'goods_index.html',locals())


