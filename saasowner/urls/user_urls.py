from django.urls import path
from saasowner.views import user_views

app_name = 'user'

urlpatterns = [
    path('users/', user_views.users, name='users'),
]