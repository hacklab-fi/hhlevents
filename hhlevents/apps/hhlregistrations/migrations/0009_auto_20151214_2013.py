# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hhlregistrations', '0008_auto_20150412_2257'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='event',
            options={'verbose_name': 'event', 'verbose_name_plural': 'events', 'ordering': ['-end_date']},
        ),
        migrations.AlterModelOptions(
            name='person',
            options={'verbose_name': 'participant', 'verbose_name_plural': 'participants', 'ordering': ['last_name']},
        ),
        migrations.AlterModelOptions(
            name='registration',
            options={'verbose_name': 'registration', 'verbose_name_plural': 'registration', 'ordering': ['event']},
        ),
        migrations.RemoveField(
            model_name='event',
            name='require_registration',
        ),
        migrations.AddField(
            model_name='event',
            name='image',
            field=models.CharField(default=0, choices=[('/static/img/3dtulostin01.png', '3dtulostin01.png'), ('/static/img/avoin_tiistai01.png', 'avoin_tiistai01.png'), ('/static/img/elektroniikka01.png', 'elektroniikka01.png'), ('/static/img/hacklab_fi01.png', 'hacklab_fi01.png'), ('/static/img/helsinkihacklab01.png', 'helsinkihacklab01.png'), ('/static/img/kokous01.png', 'kokous01.png'), ('/static/img/ompelukone01.png', 'ompelukone01.png'), ('/static/img/tyokalukasa01.png', 'tyokalukasa01.png')], max_length=100),
        ),
        migrations.AddField(
            model_name='event',
            name='registration_requirement',
            field=models.CharField(default='RQ', choices=[('RQ', 'Required'), ('OP', 'Optional'), ('NO', 'None')], max_length=2),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='registration',
            name='state',
            field=models.CharField(choices=[('AC', 'Assumed coming'), ('CC', 'Confirmed coming'), ('CP', 'Confirmed, pre-payments OK'), ('WL', 'Waiting-list'), ('CA', 'Cancelled'), ('CR', 'Cancelled, refunded'), ('WB', 'Waiting-list (due to ban)')], max_length=2),
        ),
    ]
