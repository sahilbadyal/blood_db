# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_auto_20150615_1306'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]
