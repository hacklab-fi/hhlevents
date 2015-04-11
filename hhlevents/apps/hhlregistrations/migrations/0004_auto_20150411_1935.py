# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hhlregistrations', '0003_auto_20150411_1919'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='event_cost',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='event',
            name='materials_cost',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='event',
            name='materials_mandatory',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='registration',
            name='wants_materials',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='registration',
            name='paid',
            field=models.DateTimeField(null=True, blank=True),
        ),
    ]
