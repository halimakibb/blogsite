# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-06 04:52
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20160106_1151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='updated',
            field=models.DateField(default=datetime.date.today, editable=False),
        ),
    ]
