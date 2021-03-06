from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth.views import login, logout

from . import views

urlpatterns = [
    url(r'^login/$', login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', logout, {'template_name': 'logout.html'}, name='logout'),
    url(r'^register/$', views.register, name='register'),
    url(r'^$', views.PostListView.as_view(), name='post_list'),
    url(r'^category/add/$', views.CategoryCreateView.as_view(), name='add_category'),

    url(r'^category/(?P<pk>[0-9]+)/delete$', views.CategoryDelete.as_view(), name='category_delete'),
  
    url(r'^category/(?P<pk_category>[0-9]+)/$', views.CategoryPostList.as_view(), name='category_post_list'),
    url(r'^category/(?P<pk_category>[0-9]+)/edit$', views.CategoryUpdateView.as_view(), name='edit_category'),
    url(r'^category/(?P<pk_category>[0-9]+)/post/(?P<pk_post>[0-9]+)/$', views.PostDetail.as_view(), name='post_detail'),
    url(r'^category/(?P<pk_category>[0-9]+)/post/(?P<pk_post>[0-9]+)/update$', views.PostUpdate.as_view(), name='post_update'),
    url(r'^frontpage/$', views.CategoryPostList.as_view(), name='category_post_list'),
    url(r'^user/stalk/(?P<username>\w+)/$', views.UserProfile.as_view(), name='user_profile'),
    url(r'^user/edit/$', views.EditUserProfile.as_view(), name='edit_user_profile'),
    url(r'^category/(?P<pk>[0-9]+)/$', views.CategoryPostList.as_view(), name='category_post_list'),
    url(r'^frontpage/$', views.CategoryPostList.as_view(), name='category_post_list'),
    url(r'^ajax/category_statistics/(?P<pk>[0-9]+)/$', views.get_statistics, name='category_statistics'),
    url(r'^ajax/category_follow/(?P<pk_category>[0-9]+)/(?P<username>\w+)/$', views.category_follow, name='category_follow'),
    url(r'^post_add/$', views.PostCreateView.as_view(), name='post_create'),
    url(r'^post/(?P<pk>[0-9]+)/delete$', views.PostDelete.as_view(), name='post_delete'),
    url(r'^category/(?P<pk_category>[0-9]+)/post/(?P<pk_post>[0-9]+)/comment/(?P<pk_comment>[0-9]+)/edit/$', views.CommentUpdate.as_view(),
     name='comment_update'),
    url(r'^category/(?P<pk_category>[0-9]+)/post/(?P<pk_post>[0-9]+)/comment_add/$', views.CommentCreateView.as_view(),
     name='comment_create'),
]
