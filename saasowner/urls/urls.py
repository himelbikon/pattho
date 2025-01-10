from django.urls import path
from saasowner.views import views

app_name = 'saasowner'

urlpatterns = [
    path('', views.index, name='index'),
]