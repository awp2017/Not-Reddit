# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from Readit.models import UserProfile
from Readit.models import Post, Category
from Readit.models import Comment, CommentVote
from Readit.models import PostVote

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Category)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(CommentVote)
admin.site.register(PostVote)