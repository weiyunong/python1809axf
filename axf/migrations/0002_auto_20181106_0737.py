# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-11-06 07:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('axf', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
                ('isselect', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'axf_cart',
            },
        ),
        migrations.CreateModel(
            name='Foodtypes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('typeid', models.CharField(max_length=8)),
                ('typename', models.CharField(max_length=100)),
                ('childtypenames', models.CharField(max_length=256)),
                ('typesort', models.IntegerField()),
            ],
            options={
                'db_table': 'axf_foodtypes',
            },
        ),
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productid', models.CharField(max_length=10)),
                ('productimg', models.CharField(max_length=100)),
                ('productname', models.CharField(max_length=100)),
                ('productlongname', models.CharField(max_length=100)),
                ('isxf', models.BooleanField(default=False)),
                ('pmdesc', models.BooleanField(default=False)),
                ('specifics', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=7)),
                ('marketprice', models.DecimalField(decimal_places=2, max_digits=7)),
                ('categoryid', models.IntegerField()),
                ('childcid', models.IntegerField()),
                ('childcidname', models.CharField(max_length=100)),
                ('dealerid', models.CharField(max_length=10)),
                ('storenums', models.IntegerField()),
                ('productnum', models.IntegerField()),
            ],
            options={
                'db_table': 'axf_goods',
            },
        ),
        migrations.CreateModel(
            name='MainShow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trackid', models.CharField(max_length=8)),
                ('name', models.CharField(max_length=100)),
                ('img', models.CharField(max_length=100)),
                ('categoryid', models.CharField(max_length=8)),
                ('brandname', models.CharField(max_length=50)),
                ('img1', models.CharField(max_length=100)),
                ('childcid1', models.CharField(max_length=8)),
                ('productid1', models.CharField(max_length=8)),
                ('longname1', models.CharField(max_length=100)),
                ('price1', models.FloatField()),
                ('marketprice1', models.FloatField()),
                ('img2', models.CharField(max_length=100)),
                ('childcid2', models.CharField(max_length=8)),
                ('productid2', models.CharField(max_length=8)),
                ('longname2', models.CharField(max_length=100)),
                ('price2', models.FloatField()),
                ('marketprice2', models.FloatField()),
                ('img3', models.CharField(max_length=100)),
                ('childcid3', models.CharField(max_length=8)),
                ('productid3', models.CharField(max_length=8)),
                ('longname3', models.CharField(max_length=100)),
                ('price3', models.FloatField()),
                ('marketprice3', models.FloatField()),
            ],
            options={
                'db_table': 'axf_mainshow',
            },
        ),
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('trackid', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'axf_shop',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account', models.CharField(max_length=80, unique=True)),
                ('password', models.CharField(max_length=256)),
                ('name', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=20, unique=True)),
                ('addr', models.CharField(max_length=256)),
                ('img', models.CharField(max_length=100)),
                ('rank', models.IntegerField(default=1)),
                ('token', models.CharField(max_length=256)),
            ],
            options={
                'db_table': 'axf_user',
            },
        ),
        migrations.AddField(
            model_name='cart',
            name='goods',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='axf.Goods'),
        ),
        migrations.AddField(
            model_name='cart',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='axf.User'),
        ),
    ]
