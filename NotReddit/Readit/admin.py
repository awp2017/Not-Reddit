# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from Readit.models import UserProfile
from Readit.models import Post

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Post)