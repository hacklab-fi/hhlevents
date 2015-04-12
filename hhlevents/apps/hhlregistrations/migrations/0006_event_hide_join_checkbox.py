# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hhlregistrations', '0005_auto_20150412_1806'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='hide_join_checkbox',
            field=models.BooleanField(default=False),
        ),
    ]
