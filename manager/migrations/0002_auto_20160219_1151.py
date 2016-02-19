# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-19 11:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='doc_url',
            field=models.CharField(blank=True, max_length=1024, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='img_url',
            field=models.CharField(blank=True, max_length=1024, null=True),
        ),
        migrations.AddField(
            model_name='spectrumanalyzer',
            name='freq_stop',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='spectrumanalyzer',
            name='input_power_max',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=1024),
        ),
        migrations.AlterField(
            model_name='item',
            name='name',
            field=models.CharField(max_length=1024),
        ),
        migrations.AlterField(
            model_name='spectrumanalyzer',
            name='freq_start',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
