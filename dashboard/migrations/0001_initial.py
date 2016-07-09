# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-09 19:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectSummary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filter_id', models.IntegerField()),
                ('incomplete', models.IntegerField()),
                ('complete', models.IntegerField()),
                ('total', models.IntegerField()),
                ('created_on', models.DateField()),
            ],
            options={
                'verbose_name': 'project summary',
                'verbose_name_plural': 'project summaries',
            },
        ),
        migrations.AlterUniqueTogether(
            name='projectsummary',
            unique_together=set([('filter_id', 'created_on')]),
        ),
    ]