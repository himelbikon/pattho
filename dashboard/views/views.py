from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from course import models as course_models

@login_required
def index(request):
    return render(request, 'dashboard/index/index.html')

@login_required
def be_an_instructor(request):
    course_categories = course_models.CourseCategory.objects.all()
    context = {
        'course_categories': course_categories,
    }
    return render(request, 'dashboard/be_an_instructor/index.html', context)
