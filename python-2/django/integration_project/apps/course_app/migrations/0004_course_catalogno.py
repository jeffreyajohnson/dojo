# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-21 21:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course_app', '0003_auto_20161121_1517'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='catalogNo',
            field=models.SmallIntegerField(default=100),
            preserve_default=False,
        ),
    ]
