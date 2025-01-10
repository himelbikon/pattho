from django.shortcuts import render

def index(request):
    return render(request, 'saasowner/index/index.html')
