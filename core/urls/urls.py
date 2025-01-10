from django.urls import path
from core.views import views

app_name = 'core'

urlpatterns = [
    path('', views.index, name='index'),
]