# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView 


from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User

from django.urls import reverse
from Readit.models import Post, Category, UserProfile, Comment
from Readit.forms import PostEditForm, RegistrationForm, EditUserProfile, CommentEditForm, PostAddForm


# Create your views here.

# View-urile lui Claudiu

class PostCreateView(LoginRequiredMixin, CreateView):
    template_name = 'post_add.html'
    form_class = PostAddForm
    model = Post

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(PostCreateView, self).form_valid(form)

    def get_success_url(self, *args, **kwargs):
        return reverse(
            'post_detail', 
            kwargs={
                'pk': self.object.pk
            }
        )

class PostListView(ListView):
    template_name = 'post_list.html'
    model = Post
    context_object_name = 'posts'

    def get_queryset(self, *args, **kwargs):
        return Post.objects.all()


class CategoryPostList(ListView):
    template_name = 'post_list.html'
    model = Post
    context_object_name = 'posts'

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
        return get_object_or_404(Post, pk=self.kwargs['pk_post'], category__pk=self.kwargs['pk_category'])

    def get_context_data(self, **kwargs):
        data = super(PostDetail, self).get_context_data(**kwargs)
        data['comments_list'] = Comment.objects.filter(post__id=self.kwargs['pk_post'])
        return data

class PostUpdate(UpdateView):
    model = Post
    form_class = PostEditForm
    template_name = 'post_update.html'
    pk_url_kwarg = 'pk_post'

    def get_success_url(self, *args, **kwargs):
        return reverse('post_detail', kwargs={'pk_post': self.object.pk, 'pk_category': self.kwargs['pk_category']})

class CommentUpdate(UpdateView):
    model = Comment
    form_class = CommentEditForm
    template_name = 'comment_update.html'
    pk_url_kwarg = 'pk_comment'

    def get_success_url(self, *args, **kwargs):
        return reverse('post_detail', kwargs={'pk_post': self.object.post.pk, 'pk_category': self.kwargs['pk_category']})

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
