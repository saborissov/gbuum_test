# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-05 16:19
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('primer', '0009_auto_20170705_1910'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='feedback',
            options={'ordering': ['-create'], 'verbose_name': 'Заявки'},
        ),
    ]
