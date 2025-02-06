from django.urls import path, include
from saasowner.views import views

app_name = 'saasowner'

urlpatterns = [
    path('', views.index, name='index'),
    path('users/' , include('saasowner.urls.user_urls')),
]