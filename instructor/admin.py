from django.contrib import admin
from . import models as instructor_models

models_to_show = [
    instructor_models.Instructor,
]

admin.site.register(models_to_show)
# for model in models_to_show:
#     admin.site.register(model)
