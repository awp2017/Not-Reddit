# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView 

import datetime
from django.utils import timezone

from django.views.generic.base import ContextMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User

from django.http import JsonResponse

from django.urls import reverse
from Readit.models import Post, Category, UserProfile, Comment
from Readit.forms import PostEditForm, RegistrationForm, EditUserProfile, CommentEditForm, PostAddForm, CategoryForm


# Create your views here.

# View-urile lui Claudiu

class CategoriesMixin(ContextMixin):
    def get_context_data(self, **kwargs):
        context = super(CategoriesMixin, self).get_context_data(**kwargs)
        context['all_categories'] = Category.objects.all()
        return context


class PostCreateView(LoginRequiredMixin, CategoriesMixin, CreateView):
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
                'pk_post': self.object.pk,
                'pk_category': self.object.category.pk
            }
        )
class PostListView(CategoriesMixin, ListView):
    template_name = 'post_list.html'
    model = Post
    context_object_name = 'posts'

    def get_queryset(self, *args, **kwargs):
        return Post.objects.all()


class CategoryPostList(CategoriesMixin, ListView):
    template_name = 'category_detail.html'
    model = Post
    context_object_name = 'posts'
  
    def get_context_data(self, **kwargs):
        context = super(CategoriesMixin, self).get_context_data(**kwargs)
        context['all_categories'] = Category.objects.all()
        context['posts'] = Post.objects.filter(category=self.kwargs['pk_category'])
        context['category'] = Category.objects.get(pk=self.kwargs['pk_category'])
        return context

    def get_queryset(self, *args, **kwargs):
        return Post.objects.filter(category=self.kwargs['pk_category'])


class FollowedCategoriesPostList(CategoriesMixin, ListView):
    template_name = 'post_list.html'
    model = Post
    context_object_name = 'posts'

    def get_queryset(self, *args, **kwargs):
        # TODO change user=1 to something smart
        return Post.objects.filter(category=self.kwargs['pk'], user=1)

class CategoryList(CategoriesMixin, ListView):
    template_name = 'layout.html'
    model = Category
    context_object_name = 'category_list'

    def get_queryset(self, *args, **kwargs):
        return Category.objects.all()


# View-urile Mădălinei

class PostDetail(CategoriesMixin, LoginRequiredMixin, DetailView):
    model = Post
    context_object_name = 'post_detail'
    template_name = 'post_detail.html'

    def get_object(self):
        return get_object_or_404(Post, pk=self.kwargs['pk_post'], category__pk=self.kwargs['pk_category'])

    def get_context_data(self, **kwargs):
        data = super(PostDetail, self).get_context_data(**kwargs)
        data['comments_list'] = Comment.objects.filter(post__id=self.kwargs['pk_post'])
        return data

class PostUpdate(CategoriesMixin, LoginRequiredMixin, UpdateView):
    model = Post
    form_class = PostEditForm
    template_name = 'post_update.html'
    pk_url_kwarg = 'pk_post'

    def get_success_url(self, *args, **kwargs):
        return reverse('post_detail', kwargs={'pk_post': self.object.pk, 'pk_category': self.kwargs['pk_category']})

class CommentUpdate(CategoriesMixin, LoginRequiredMixin, UpdateView):
    model = Comment
    form_class = CommentEditForm
    template_name = 'comment_update.html'
    pk_url_kwarg = 'pk_comment'

    def get_success_url(self, *args, **kwargs):
        return reverse('post_detail', kwargs={'pk_post': self.object.post.pk, 'pk_category': self.kwargs['pk_category']})

class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentEditForm
    template_name = 'comment_create.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.post = get_object_or_404(Post, pk=self.kwargs['pk_post'], category__pk=self.kwargs['pk_category'])
        return super(CommentCreateView, self).form_valid(form)

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


def category_follow(request, pk_category, username):
    if request.method == 'GET':
        category = Category.objects.get(pk=pk_category)
        user = User.objects.get(username=username)
        print pk_category

        if not (user in category.followers.all()):
            category.followers.add(user)
        else:
            category.followers.remove(user)
        category.save()
        return JsonResponse({})



class UserProfile(CategoriesMixin, DetailView):
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

class CategoryCreateView(LoginRequiredMixin, CreateView):
    template_name = 'category_form.html'
    form_class = CategoryForm
    model = Category

    def get_success_url(self, *args, **kwargs):
        return reverse(
            'category_post_list', 
            kwargs = {
                'pk_category': self.object.pk
            }
        )

class CategoryUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'category_form.html'
    form_class = CategoryForm
    model = Category
    pk_url_kwarg = 'pk_category'

    def get_success_url(self, *args, **kwargs):
        return reverse(
            'category_post_list', 
            kwargs = {
                'pk_category': self.object.pk
            }
        )

# View-urile lui Dutzu

class UserProfileDetail(CategoriesMixin, DetailView):
    model = UserProfile
    context_object_name = 'user_profile_detail'
    template_name = 'user_profile_detail.html'

    def get_object(self):
        return get_object_or_404(UserProfile, pk=self.kwargs['pk'])

class PostDelete(LoginRequiredMixin, DeleteView):
    template_name = 'post_delete.html'
    model = Post
    
    def get_success_url(self, *args, **kwargs):
        return reverse('post_list')

class CategoryDelete(LoginRequiredMixin, DeleteView):
    template_name = 'category_delete.html'
    model = Category
    
    def get_success_url(self, *args, **kwargs):
        return reverse('post_list')

