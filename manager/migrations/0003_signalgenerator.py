# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-19 13:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0002_auto_20160219_1151'),
    ]

    operations = [
        migrations.CreateModel(
            name='SignalGenerator',
            fields=[
                ('item_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='manager.Item')),
                ('freq_start', models.IntegerField(blank=True, null=True)),
                ('freq_stop', models.IntegerField(blank=True, null=True)),
                ('output_power_max', models.IntegerField(blank=True, null=True)),
            ],
            bases=('manager.item',),
        ),
    ]
