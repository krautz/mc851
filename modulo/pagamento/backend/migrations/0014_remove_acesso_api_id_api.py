# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-10-31 18:59
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0013_auto_20181031_1858'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='acesso_api',
            name='id_API',
        ),
    ]
