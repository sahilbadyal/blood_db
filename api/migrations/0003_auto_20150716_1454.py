# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20150716_1453'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donor',
            name='rh_factor',
            field=models.CharField(max_length=1, verbose_name=b'rh'),
        ),
    ]
