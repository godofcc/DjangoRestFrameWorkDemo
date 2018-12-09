# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-12-08 10:21
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('index', models.IntegerField(default=0)),
                ('add_time', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goods_sn', models.CharField(blank=True, max_length=30, null=True)),
                ('name', models.CharField(blank=True, max_length=30, null=True)),
                ('click_num', models.IntegerField(default=0)),
                ('sold_num', models.IntegerField(default=0)),
                ('fav_num', models.IntegerField(default=0)),
                ('goods_num', models.IntegerField(default=0)),
                ('market_price', models.FloatField(default=0)),
                ('shope_price', models.FloatField(default=0)),
                ('goods_brief', models.TextField()),
                ('goods_desc', models.TextField()),
                ('ship_free', models.BooleanField(default=False)),
                ('is_new', models.BooleanField(default=False)),
                ('is_hot', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='GoodsCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=30, null=True)),
                ('code', models.CharField(blank=True, max_length=30, null=True)),
                ('desc', models.TextField()),
                ('category_type', models.IntegerField(choices=[(1, 'First'), (2, 'Second'), (3, 'Third')])),
                ('is_tab', models.BooleanField(default=False, help_text='是否导航')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now)),
                ('parent_category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Goods.GoodsCategory')),
            ],
            options={
                'verbose_name': 'Goods',
            },
        ),
        migrations.CreateModel(
            name='GoodsCategoryBrand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=30, null=True)),
                ('desc', models.TextField()),
                ('add_time', models.DateTimeField(default=datetime.datetime.now)),
            ],
            options={
                'verbose_name': 'Brand',
            },
        ),
        migrations.CreateModel(
            name='GoodsImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_time', models.DateTimeField(verbose_name=datetime.datetime.now)),
                ('goods', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Goods.Goods')),
            ],
            options={
                'verbose_name': 'Picture',
            },
        ),
        migrations.AddField(
            model_name='goods',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Goods.GoodsCategory'),
        ),
        migrations.AddField(
            model_name='banner',
            name='goods',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Goods.Goods'),
        ),
    ]