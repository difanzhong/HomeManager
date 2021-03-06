# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-08-27 13:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Houses', '0004_auto_20170820_1139'),
    ]

    operations = [
        migrations.CreateModel(
            name='CreditCard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('VISA', 'VISA'), ('MasterCard', 'MasterCard')], max_length=10)),
                ('card_number', models.CharField(max_length=16)),
                ('cvv', models.CharField(max_length=3)),
                ('expire_month', models.CharField(choices=[('JAN', '01'), ('FEB', '02'), ('MAR', '03'), ('APR', '04'), ('MAY', '05'), ('JUN', '06'), ('JUL', '07'), ('AUG', '08'), ('SEP', '09'), ('OCT', '10'), ('NOV', '11'), ('DEC', '12')], max_length=3)),
                ('expire_year', models.CharField(choices=[('18', '2018'), ('19', '2019'), ('20', '2020'), ('21', '2021'), ('22', '2022'), ('23', '2023')], max_length=4)),
            ],
        ),
    ]
