# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-25 03:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0005_remove_student_region'),
    ]

    operations = [
        migrations.CreateModel(
            name='StaffContact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note', models.TextField()),
                ('conversation_date_time', models.DateTimeField(help_text='Example format: 10/25/2006 14:30')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='students.Student')),
            ],
        ),
    ]
