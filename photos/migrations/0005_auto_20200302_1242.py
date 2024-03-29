# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-03-02 09:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0004_auto_20200302_1155'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='phone_number',
        ),
        migrations.RemoveField(
            model_name='image',
            name='category',
        ),
        migrations.AddField(
            model_name='image',
            name='category',
            field=models.ManyToManyField(to='photos.category'),
        ),
        migrations.AlterField(
            model_name='image',
            name='photo',
            field=models.ImageField(blank=True, upload_to='photos/'),
        ),
    ]
