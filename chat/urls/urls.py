from django.urls import path
from chat.views import views

app_name = 'chat'

urlpatterns = [
    path('', views.index, name='index'),
    path('inbox/<str:room_uuid>', views.inbox, name='inbox'),
]