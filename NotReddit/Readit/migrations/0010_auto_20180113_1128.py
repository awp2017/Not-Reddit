# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-13 11:28
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Readit', '0009_category_admins'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='admin',
            name='category',
        ),
        migrations.RemoveField(
            model_name='admin',
            name='user',
        ),
        migrations.RemoveField(
            model_name='followcategory',
            name='category',
        ),
        migrations.RemoveField(
            model_name='followcategory',
            name='user',
        ),
        migrations.AddField(
            model_name='category',
            name='followers',
            field=models.ManyToManyField(related_name='followed_categories', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='comment',
            name='votes',
            field=models.ManyToManyField(related_name='voted_comments', through='Readit.CommentVote', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='post',
            name='votes',
            field=models.ManyToManyField(related_name='voted_posts', through='Readit.PostVote', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='category',
            name='admins',
            field=models.ManyToManyField(related_name='admined_categories', to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Admin',
        ),
        migrations.DeleteModel(
            name='FollowCategory',
        ),
    ]
