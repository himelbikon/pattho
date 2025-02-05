from django.shortcuts import render

def index(request):
    return render(request, 'chat/index/index.html')

def inbox(request, room_uuid):
    return render(request, 'chat/inbox/index.html')