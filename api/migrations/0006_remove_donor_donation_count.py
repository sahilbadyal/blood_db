# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_donor_donation_count'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='donor',
            name='donation_count',
        ),
    ]
