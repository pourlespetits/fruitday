# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-08-06 08:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0013_auto_20180726_2136'),
    ]

    operations = [
        migrations.CreateModel(
            name='CartInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField(verbose_name='购买数量')),
                ('goodid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='index.Goods', verbose_name='商品ID')),
                ('userid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='index.Users', verbose_name='用户ID')),
            ],
            options={
                'verbose_name': '购物车',
                'verbose_name_plural': '购物车',
                'db_table': 'cartinfo',
                'ordering': ('-count',),
            },
        ),
    ]