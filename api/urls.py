from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('users', views.users_index, name='users'),
    path('users/<int:pk>', views.users_show, name='user'),
]
