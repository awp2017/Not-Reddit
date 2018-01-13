# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, get_object_or_404 
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView 
from Readit.models import Post , UserProfile
from Readit.forms import MyForm

# Create your views here.

# View-urile lui Claudiu

class PostListView(ListView):
    template_name = 'home.html'
    model = Post
    context_object_name = 'posts'

    def get_queryset(self, *args, **kwargs):
        return Post.objects.all()


# View-urile Mădălinei

class PostDetail(DetailView):
    model = Post
    context_object_name = 'post_detail'
    template_name = 'post_detail.html'

    def get_object(self):
        return get_object_or_404(Post, pk=self.kwargs['pk'])


# View-urile Dianei

def register(request):
    if request.method =='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        return render(request, 'registration.html', {'form': form})
    else:
        form = UserCreationForm()
        return render(request, 'registration.html', {'form': form})


# View-urile lui Dutzu

class UserProfileDetail(DetailView):
    model = UserProfile
    context_object_name = 'user_profile_detail'
    template_name = 'user_profile_detail.html'

    def get_object(self):
        return get_object_or_404(UserProfile, pk=self.kwargs['pk'])
