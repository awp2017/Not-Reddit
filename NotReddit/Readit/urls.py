from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth.views import login

from . import views

urlpatterns = [
    url(r'^login/$', login, {'template_name': 'login.html'}, name='login'),
    url(r'^register/$', views.register, name='register'),
    url(r'^$', views.PostListView.as_view(), name='post_list'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.PostDetail.as_view(), name='post_detail'),
    url(r'^user/(?P<pk>[0-9]+)/$', views.UserProfileDetail.as_view(), name='user_detail'),
]
