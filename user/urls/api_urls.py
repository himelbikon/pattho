from django.urls import path
from user.views import api_views

app_name = 'api'

urlpatterns = [
    path('login/', api_views.login_api, name='login'),
]