from django.urls import path
from dashboard.views import views

app_name = 'dashboard'

urlpatterns = [
    path('', views.index, name='index'),
]