# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-18 19:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jirani', '0013_remove_post_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='business',
            name='profile',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='jirani.Profile'),
        ),
    ]