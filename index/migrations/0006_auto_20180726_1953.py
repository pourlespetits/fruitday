# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-07-26 11:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0005_auto_20180726_1942'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UsersAdmin',
        ),
        migrations.AlterField(
            model_name='goods',
            name='isActive',
            field=models.BooleanField(default=True, verbose_name='销售状态'),
        ),
        migrations.AlterField(
            model_name='goods',
            name='picture',
            field=models.ImageField(upload_to='static/upload/goods', verbose_name='图示'),
        ),
        migrations.AlterField(
            model_name='goods',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='商品价格'),
        ),
        migrations.AlterField(
            model_name='goods',
            name='spec',
            field=models.CharField(max_length=50, verbose_name='商品规格'),
        ),
        migrations.AlterField(
            model_name='goods',
            name='title',
            field=models.CharField(max_length=30, verbose_name='商品名称'),
        ),
    ]
