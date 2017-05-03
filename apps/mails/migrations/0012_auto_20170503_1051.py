# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-03 10:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mails', '0011_mail_template'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mail',
            name='template',
            field=models.ForeignKey(help_text='The used template', on_delete=django.db.models.deletion.CASCADE, to='mails.MailTemplate', verbose_name='Used Mail template'),
        ),
        migrations.AlterField(
            model_name='mail',
            name='time_delivered',
            field=models.DateTimeField(blank=True, editable=False, help_text='Actual delivery time by the email backend', null=True, verbose_name='Delivery time'),
        ),
    ]