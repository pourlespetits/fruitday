# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-08-06 08:23
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0014_cartinfo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cartinfo',
            old_name='goodid',
            new_name='good',
        ),
        migrations.RenameField(
            model_name='cartinfo',
            old_name='userid',
            new_name='user',
        ),
    ]
