# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hhlregistrations', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='extra_url',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='gforms_url',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='max_registrations',
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]
