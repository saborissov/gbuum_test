# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-10 10:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('primer', '0016_auto_20170710_1325'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback_done',
            name='cтатус',
            field=models.CharField(choices=[('Выполнено', 'Выполнено')], default='Выполнено', max_length=125),
        ),
    ]
