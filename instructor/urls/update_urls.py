from django.urls import path
from instructor.views import update_views

app_name = 'update'

urlpatterns = [
    path('instructor-category/', update_views.update_instructor_category, name='update_instructor_category'),
]