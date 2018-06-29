from .models import Notification, User

def notify(request):
    if request.session.get('username'):
        user = User.objects.get(username=request.session.get('username'))
        notis = Notification.objects.filter(aim_user=user).filter(have_read=False)
        n = len(notis)
        if n != 0:
            return {'lang': n}
    return {}   