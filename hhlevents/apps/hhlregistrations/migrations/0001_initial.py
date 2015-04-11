# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('happenings', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('event_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='happenings.Event')),
                ('extra_url', models.URLField()),
                ('gforms_url', models.URLField()),
                ('max_registrations', models.PositiveSmallIntegerField()),
            ],
            bases=('happenings.event',),
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=150)),
                ('last_name', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('paid', models.DateTimeField(null=True)),
                ('registered', models.DateTimeField(default=datetime.datetime.now)),
                ('cancelled', models.DateTimeField(null=True)),
                ('state', models.CharField(max_length=2, choices=[(b'AC', b'Assumed coming'), (b'CC', b'Confirmed coming'), (b'WL', b'Waiting-list'), (b'CA', b'Cancelled')])),
                ('event', models.ForeignKey(related_name='persons', to='hhlregistrations.Event')),
                ('person', models.ForeignKey(related_name='events', to='hhlregistrations.Person')),
            ],
        ),
    ]
