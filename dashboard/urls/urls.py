from django.urls import path
from dashboard.views import views

app_name = 'dashboard'

urlpatterns = [
    path('', views.index, name='index'),
    path('be-an-instructor/', views.be_an_instructor, name='be_an_instructor'),
]