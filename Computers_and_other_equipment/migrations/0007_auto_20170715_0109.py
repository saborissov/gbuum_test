# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-14 22:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Computers_and_other_equipment', '0006_list_of_printer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartridge_list',
            name='catlis_printerId',
        ),
        migrations.AddField(
            model_name='cartridge_list',
            name='catlis_printer',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='Computers_and_other_equipment.Принтер', verbose_name='Модель принтеров'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='cartridge_list',
            name='catlis_cartridge',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Computers_and_other_equipment.Картридж', verbose_name='Модель картриджей'),
        ),
    ]
