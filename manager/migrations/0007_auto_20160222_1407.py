# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-22 14:07
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0006_reservation'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='reserved_by',
        ),
        migrations.RemoveField(
            model_name='item',
            name='reserved_until',
        ),
    ]