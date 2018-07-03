from django.http import HttpResponseRedirect
from django.contrib import messages

def login_required(func):
    def wrapper(request, *args, **kwargs):
        if request.session.get('username'):
            return func(request, *args, **kwargs)
        else:
            messages.error(request, '请先登录')
            return HttpResponseRedirect('/')
    return wrapper
