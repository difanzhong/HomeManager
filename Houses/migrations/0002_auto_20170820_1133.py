# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-20 01:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Houses', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='customer',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='Houses.Customer'),
        ),
        migrations.AlterField(
            model_name='address',
            name='house',
            field=models.OneToOneField(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='Houses.House'),
        ),
    ]
