# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=10000, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    admins = models.ManyToManyField(User, related_name='admined_categories')
    followers = models.ManyToManyField(User, related_name='followed_categories')

    def __str__(self):
        return self.name


class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name='profile')
    description = models.CharField(max_length=200)
    image_url = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.user.username


# Trigger for creating an User Profile object for a new user.
def create_user_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = UserProfile.objects.create(user=kwargs['instance'])


post_save.connect(create_user_profile, sender=User)


class Post(models.Model):
    class Meta:
        ordering = ('-date_created',)

    category = models.ForeignKey(Category)
    user = models.ForeignKey(User)
    title = models.CharField(max_length=100)
    text = models.CharField(max_length=500, blank=True)
    link = models.URLField(max_length=100, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    votes = models.ManyToManyField(User, through='PostVote', related_name="voted_posts")
    # TODO: Add post image

    def __str__(self):
        return self.title


class Comment(models.Model):
    text = models.CharField(max_length=10000)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User)
    post = models.ForeignKey(Post)
    #comment = models.ForeignKey('self', related_name='+', blank=True)
    votes = models.ManyToManyField(User, through='CommentVote', related_name="voted_comments")

    def __str__(self):
        return self.text


class CommentVote(models.Model):
    type = models.IntegerField()
    user = models.ForeignKey(User)
    comment = models.ForeignKey(Comment, related_name='+')

    def __str__(self):
        return self.type


class PostVote(models.Model):
    type = models.IntegerField()
    user = models.ForeignKey(User)
    post = models.ForeignKey(Post)

    def __str__(self):
        return self.type

