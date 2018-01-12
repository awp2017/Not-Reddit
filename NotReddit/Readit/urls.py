from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth.views import login

urlpatterns = [
    url(r'^login/$', login, {'template_name': 'login.html'}, name='login'),
]
