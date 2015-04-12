# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hhlregistrations', '0004_auto_20150411_1935'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='payment_due',
            field=models.DateTimeField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='event',
            name='require_registration',
            field=models.BooleanField(default=False),
        ),
    ]
