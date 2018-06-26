from django.shortcuts import render

# Create your views here.
<<<<<<< HEAD
def market_views(request):
    if request.method == 'GET':
        return render(request,'market.html',locals())
=======
def index_views(request):
    return render(request,'market_index.html')
>>>>>>> main/master
