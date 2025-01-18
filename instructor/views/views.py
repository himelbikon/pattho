from django.shortcuts import render, redirect
from instructor import models as instructor_models
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.contrib.auth.decorators import login_required 


@require_POST
@login_required
def become_an_instructor(request):
    if request.user.is_instructor:
        return redirect('dashboard:be_an_instructor')

    instructor = instructor_models.Instructor(user=request.user)
    instructor.save()
    messages.success(request, 'You are now an Instructor')
    return redirect('dashboard:be_an_instructor')