# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2018-03-25 09:57
from __future__ import unicode_literals

import django.core.serializers.json
from django.db import migrations
import taiga.base.db.models.fields.json


class Migration(migrations.Migration):

    dependencies = [
        ('userstories', '0015_publish_date_time_fields'),
    ]

    operations = [
        migrations.AddField(
            model_name='userstory',
            name='social_media_attributes',
            field=taiga.base.db.models.fields.json.JSONField(blank=True, encoder=django.core.serializers.json.DjangoJSONEncoder, null=True, verbose_name='social media attributes'),
        ),
    ]
