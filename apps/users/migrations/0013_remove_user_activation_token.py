# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-06-10 16:35
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_auto_20170527_1348'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='activation_token',
        ),
    ]
