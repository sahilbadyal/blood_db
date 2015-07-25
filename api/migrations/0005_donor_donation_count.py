# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20150717_1105'),
    ]

    operations = [
        migrations.AddField(
            model_name='donor',
            name='donation_count',
            field=models.IntegerField(default=0, verbose_name=b'Number of Donations'),
        ),
    ]
