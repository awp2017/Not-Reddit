# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-13 09:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Readit', '0005_admin_followcategory'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='last_name',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='image_url',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]