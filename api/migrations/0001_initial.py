# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Donor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('blood_group', models.CharField(max_length=2, choices=[(b'A', b'A'), (b'B', b'B'), (b'O', b'O'), (b'AB', b'AB')])),
                ('rh_factor', models.BooleanField()),
                ('phone_no', models.CharField(max_length=13)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.CharField(max_length=50, null=True)),
                ('last_donation', models.DateField()),
                ('birth_year', models.IntegerField()),
            ],
        ),
    ]
