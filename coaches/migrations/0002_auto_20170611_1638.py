# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-11 13:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coaches', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coach',
            name='address',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='coach',
            name='description',
            field=models.TextField(),
        ),
    ]
