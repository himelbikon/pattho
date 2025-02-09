from django.shortcuts import render
from chat import models as chat_models

def index(request):
    rooms = chat_models.Room.objects.filter(users=request.user)
    context = {
        'rooms': rooms
    }
    return render(request, 'chat/index/index.html', context)

def inbox(request, room_uuid):
    room = chat_models.Room.objects.get(uuid=room_uuid)
    context = {
        'room': room,
        'messages': room.messages.all(),
    }
    return render(request, 'chat/inbox/index.html', context)