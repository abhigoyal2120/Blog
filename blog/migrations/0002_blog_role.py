# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-12-06 12:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='role',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='user.Role'),
        ),
    ]
