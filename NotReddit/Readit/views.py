# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView 

import datetime
from django.utils import timezone


from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User

from django.http import JsonResponse

from django.urls import reverse
from Readit.models import Post, UserProfile, Category, UserProfile
from Readit.forms import PostEditForm, RegistrationForm, EditUserProfile


# Create your views here.

# View-urile lui Claudiu


class PostListView(ListView):
    template_name = 'post_list.html'
    model = Post
    context_object_name = 'posts'

    def get_queryset(self, *args, **kwargs):
        return Post.objects.all()


class CategoryPostList(ListView):
    template_name = 'category_detail.html'
    model = Post
    context_object_name = 'posts'
  
    def get_context_data(self, **kwargs):
        context = {}
        context['posts'] = Post.objects.filter(category=self.kwargs['pk'])
        context['category'] = Category.objects.get(pk=self.kwargs['pk'])
        return context

    def get_queryset(self, *args, **kwargs):
        return Post.objects.filter(category=self.kwargs['pk'])


class FollowedCategoriesPostList(ListView):
    template_name = 'post_list.html'
    model = Post
    context_object_name = 'posts'

    def get_queryset(self, *args, **kwargs):
        # TODO change user=1 to something smart
        return Post.objects.filter(category=self.kwargs['pk'], user=1)

class CategoryList(ListView):
    template_name = 'layout.html'
    model = Category
    context_object_name = 'category_list'

    def get_queryset(self, *args, **kwargs):
        print 'xoxoxo'
        return Category.objects.all().order_by('name')

# View-urile Mădălinei

class PostDetail(DetailView):
    model = Post
    context_object_name = 'post_detail'
    template_name = 'post_detail.html'

    def get_object(self):
        return get_object_or_404(Post, pk=self.kwargs['pk'])

class PostUpdate(UpdateView):
    model = Post
    form_class = PostEditForm
    template_name = 'post_update.html'
    
    def get_success_url(self, *args, **kwargs):
        return reverse('post_detail', kwargs={'pk': self.object.pk})

# View-urile Dianei
def register(request):
    if request.method =='POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        return render(request, 'registration.html', {'form': form})
    else:
        form = RegistrationForm()
        return render(request, 'registration.html', {'form': form})


def get_statistics(request, pk):
    if request.method == 'GET':
        result = []
        for i in range(0, 15):
            date = timezone.now() - datetime.timedelta(i)
            y = date.year;
            m = date.month;
            d = date.day;
            posts = Post.objects.filter(category=pk).filter(date_created__year=y, 
                                                            date_created__month=m, 
                                                            date_created__day=d).count()

            dateResult = date.strftime("%d-%b-%Y")
            result.append({'date': dateResult, 'posts': posts})
        return JsonResponse({'result': result})


class UserProfile(DetailView):
    model = User
    context_object_name = 'user'
    template_name = 'user_profile_detail.html'
    def get_object(self):
        return get_object_or_404(User, username=self.kwargs['username'])


class EditUserProfile(LoginRequiredMixin, UpdateView):
    template_name = 'edit_user_profile.html'
    form_class = EditUserProfile
    model = UserProfile

    def get_object(self):
    	return self.request.user.profile
    
    def get_success_url(self, *args, **kwargs):
        return reverse(
            'user_profile', 
            kwargs={
                'username': self.object.user.username
            }
        )


# View-urile lui Dutzu

class UserProfileDetail(DetailView):
    model = UserProfile
    context_object_name = 'user_profile_detail'
    template_name = 'user_profile_detail.html'

    def get_object(self):
        return get_object_or_404(UserProfile, pk=self.kwargs['pk'])
