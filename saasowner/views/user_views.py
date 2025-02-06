from django.shortcuts import render
from user import models as user_models

def users(request):
    users = user_models.User.objects.all()
    context = {
        'users': users
    }
    return render(request, 'saasowner/user/users/index.html', context)