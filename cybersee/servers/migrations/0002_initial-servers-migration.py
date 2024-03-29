# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-03 22:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('metrics', '0001_initial-metrics-migration'),
        ('servers', '0001_initial-servers-migration'),
        ('users', '0001_initial-servers-migration'),
    ]

    operations = [
        migrations.AddField(
            model_name='server',
            name='community',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='users.Community'),
        ),
    ]
