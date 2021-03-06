# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-11 12:46
from __future__ import unicode_literals

import kindred.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0006_auto_20160106_1949'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='study',
            name='is_archived',
        ),
        migrations.AddField(
            model_name='study',
            name='archived',
            field=models.DateTimeField(blank=True, help_text='When non-None, the study is archived. Archiving hides the study away so it can be forgotten about', null=True),
        ),
        migrations.AlterField(
            model_name='study',
            name='data',
            field=kindred.jsonb.JSONField(blank=True, default={}, null=True),
        ),
    ]
