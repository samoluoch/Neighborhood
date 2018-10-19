# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-19 16:29
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('jirani', '0016_business_pub_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='business',
            name='profile',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]