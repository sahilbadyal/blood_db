# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20150716_1454'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donor',
            name='address',
            field=models.CharField(max_length=100, null=True, verbose_name=b'Address'),
        ),
        migrations.AlterField(
            model_name='donor',
            name='birth_year',
            field=models.IntegerField(verbose_name=b'Birth Year'),
        ),
        migrations.AlterField(
            model_name='donor',
            name='blood_group',
            field=models.CharField(max_length=2, verbose_name=b'Blood Group', choices=[(b'A', b'A'), (b'B', b'B'), (b'O', b'O'), (b'AB', b'AB')]),
        ),
        migrations.AlterField(
            model_name='donor',
            name='email',
            field=models.EmailField(max_length=254, verbose_name=b'Email'),
        ),
        migrations.AlterField(
            model_name='donor',
            name='first_name',
            field=models.CharField(max_length=30, verbose_name=b'First Name'),
        ),
        migrations.AlterField(
            model_name='donor',
            name='last_donation',
            field=models.DateField(verbose_name=b'Last Donation'),
        ),
        migrations.AlterField(
            model_name='donor',
            name='last_name',
            field=models.CharField(max_length=30, verbose_name=b'Last Name'),
        ),
        migrations.AlterField(
            model_name='donor',
            name='phone_no',
            field=models.CharField(max_length=13, verbose_name=b'Mobile'),
        ),
        migrations.AlterField(
            model_name='donor',
            name='rh_factor',
            field=models.CharField(max_length=1, verbose_name=b'RH'),
        ),
    ]
