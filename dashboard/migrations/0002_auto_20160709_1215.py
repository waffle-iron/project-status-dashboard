# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-09 16:15
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='projectsummary',
            old_name='fetched_on',
            new_name='created_on',
        ),
    ]
