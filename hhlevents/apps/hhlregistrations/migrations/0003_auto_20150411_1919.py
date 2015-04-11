# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hhlregistrations', '0002_auto_20150411_1912'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='close_registrations',
            field=models.DateTimeField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='person',
            name='banned',
            field=models.DateTimeField(null=True, verbose_name='Automatically put to waiting list', blank=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='email',
            field=models.EmailField(unique=True, max_length=254),
        ),
        migrations.AlterField(
            model_name='registration',
            name='cancelled',
            field=models.DateTimeField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='registration',
            name='state',
            field=models.CharField(max_length=2, choices=[(b'AC', b'Assumed coming'), (b'CC', b'Confirmed coming'), (b'WL', b'Waiting-list'), (b'CA', b'Cancelled'), (b'WB', b'Waiting-list (due to ban)')]),
        ),
    ]
