# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-05 15:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('primer', '0006_auto_20170705_1845'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='статус',
            field=models.CharField(choices=[('В работе', 'В работе')], default='В работе', max_length=125),
        ),
    ]
