# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-06-04 05:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='photo',
            field=models.FileField(upload_to=''),
        ),
    ]