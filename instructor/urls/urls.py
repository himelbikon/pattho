from django.urls import path, include
from instructor.views import views

app_name = 'instructor'

urlpatterns = [
    path('u/', include('instructor.urls.update_urls')),

    path('become-an-instructor/', views.become_an_instructor, name='become_an_instructor'),
]