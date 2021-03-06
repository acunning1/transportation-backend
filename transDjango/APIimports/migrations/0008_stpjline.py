# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-05 20:43
from __future__ import unicode_literals

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APIimports', '0007_auto_20170210_0157'),
    ]

    operations = [
        migrations.CreateModel(
            name='StPJline',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('objectid', models.IntegerField()),
                ('linkpath', models.CharField(max_length=1000)),
                ('projectid', models.CharField(max_length=1000)),
                ('projectname', models.CharField(max_length=1000)),
                ('status', models.CharField(max_length=1000)),
                ('contactname', models.CharField(max_length=1000)),
                ('shape_length', models.FloatField()),
                ('geom', django.contrib.gis.db.models.fields.GeometryField(srid=4326)),
            ],
        ),
    ]
