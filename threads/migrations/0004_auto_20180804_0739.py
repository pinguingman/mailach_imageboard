# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-08-04 07:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('threads', '0003_auto_20180803_2029'),
    ]

    operations = [
        migrations.RenameField(
            model_name='section',
            old_name='section_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='thread',
            old_name='post_text',
            new_name='text',
        ),
        migrations.AddField(
            model_name='thread',
            name='title',
            field=models.CharField(default='Title', max_length=100),
        ),
    ]