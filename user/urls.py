from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from user.views import RegisterUserView


app_name = 'user'

urlpatterns = [
    path('register', RegisterUserView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
