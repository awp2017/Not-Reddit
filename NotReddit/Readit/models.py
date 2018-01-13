# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=10000, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    description = models.CharField(max_length=200)
    #TODO (dianamin): Add user image.

    def __str__(self):
        return self.user.username

class Post(models.Model):
    category = models.ForeignKey(Category)
    user = models.ForeignKey(User)
    title = models.CharField(max_length=100)
    text = models.CharField(max_length=500, blank=True)
    link = models.URLField(max_length=100, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    type = models.IntegerField(default=0, blank=True)
    #TODO: Add post image

    def __str__(self):
        return self.title


# Who admins what category
class Admin(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User)
    category = models.ForeignKey(Category)


# Who follows what category
class FollowCategory(models.Model):
    user = models.ForeignKey(User)
    category = models.ForeignKey(Category)


class Comment(models.Model):
    text = models.CharField(max_length=10000)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User)
    post = models.ForeignKey(Post)
    comment = models.ForeignKey('self', related_name='+')

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
    post= models.ForeignKey(Post)

    def __str__(self):
        return self.type

