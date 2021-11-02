from django.shortcuts import render
from .models import Room, Message
from django.utils.text import slugify
# Create your views here.


def index(request):
    rooms = Room.objects.all()
    return render(request, 'index.html', context={'rooms': rooms})


def join_room(request, room_name):
    room, created = Room.objects.get_or_create(room_name=room_name)

    message = room.messages.order_by('-timestamp')[:50]
    return render(request, 'room.html', {
        'room_name': room_name,
        'message': message,
    })
