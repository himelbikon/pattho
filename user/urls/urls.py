from django.urls import path, include
from user.views import views

app_name = 'user'

urlpatterns = [
    # api urls
    path('api/', include('user.urls.api_urls')),

    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
]