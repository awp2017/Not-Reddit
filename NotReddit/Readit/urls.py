from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth.views import login

from . import views

urlpatterns = [
    url(r'^login/$', login, {'template_name': 'login.html'}, name='login'),
    url(r'^register/$', views.register, name='register'),
]
