# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-03-03 08:20
from __future__ import unicode_literals

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0005_auto_20200302_1242'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='photo',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='image'),
        ),
    ]
