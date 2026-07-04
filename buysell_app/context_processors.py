from .models import State,Notification

def location_data(request):

    return {

        "states": State.objects.all()

    }

def notification_count(request):

    count = 0

    if request.user.is_authenticated:

        count = Notification.objects.filter(
            seller=request.user,
            is_read=False
        ).count()

    return {

        "notification_count": count

    }