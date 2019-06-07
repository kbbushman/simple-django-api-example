from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('api/v1/users', views.users_index, name='users'),
]
