# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-25 01:14
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_auto_20160919_0808'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='student',
            options={'verbose_name': 'Student Base'},
        ),
    ]
