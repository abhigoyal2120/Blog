# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-12-12 07:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20181207_1502'),
    ]

    operations = [
        migrations.CreateModel(
            name='Published_blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('published', models.BooleanField(default=True)),
            ],
        ),
        migrations.AlterModelOptions(
            name='blog',
            options={'ordering': ['-created']},
        ),
        migrations.RemoveField(
            model_name='blog',
            name='auth_group',
        ),
        migrations.AddField(
            model_name='blog',
            name='published',
            field=models.BooleanField(default=True),
        ),
    ]
