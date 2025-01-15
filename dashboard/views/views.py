from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    return render(request, 'dashboard/index/index.html')

@login_required
def be_an_instructor(request):
    return render(request, 'dashboard/be_an_instructor/index.html')
