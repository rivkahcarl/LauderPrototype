# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-25 01:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('programs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='program',
            name='event_start_date_time',
            field=models.DateTimeField(help_text='10/25/2006 14:30'),
        ),
    ]
