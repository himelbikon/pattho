from django.contrib import admin
from . import models as course_models

models_to_show = [
    course_models.CourseCategory,
]

admin.site.register(models_to_show)
