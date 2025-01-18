from django.http import JsonResponse
from course import models as course_models
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required


