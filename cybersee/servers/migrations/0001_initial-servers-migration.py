# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-03 20:58
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('metrics', '0001_initial-metrics-migration'),
    ]

    operations = [
        migrations.CreateModel(
            name='Server',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('ip_address', models.GenericIPAddressField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('metrics', models.ManyToManyField(to='metrics.Metric')),
            ],
        ),
    ]