# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-07-24 02:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('spec', models.CharField(max_length=50)),
                ('picture', models.ImageField(upload_to='static/images/')),
                ('isActive', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='GoodsType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tname', models.CharField(max_length=50)),
                ('gpicture', models.ImageField(upload_to='')),
                ('tdesc', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uphone', models.CharField(max_length=11)),
                ('upwd', models.CharField(max_length=20)),
                ('uname', models.CharField(max_length=30)),
                ('uemail', models.EmailField(max_length=254)),
                ('isActive', models.BooleanField(default=True)),
            ],
        ),
    ]