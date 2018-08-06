# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-08-06 14:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('threads', '0013_thread_video'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to='threads/static/threads/videos'),
        ),
    ]
