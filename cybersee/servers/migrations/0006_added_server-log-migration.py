# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-04 22:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('servers', '0005_add-game-migration'),
    ]

    operations = [
        migrations.CreateModel(
            name='ServerLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('recorded', models.DateTimeField(db_index=True, default=django.utils.timezone.now)),
                ('server', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='servers.Server')),
            ],
        ),
    ]
