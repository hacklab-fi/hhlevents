# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hhlregistrations', '0006_event_hide_join_checkbox'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='registration',
            unique_together=set([('event', 'person')]),
        ),
    ]
