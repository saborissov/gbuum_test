# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-10 09:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('primer', '0010_auto_20170705_1919'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback_done',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cтатус', models.CharField(choices=[('Выполнено', 'Выполнено')], default='Выполнено', max_length=125)),
                ('номер_заявки', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='primer.Feedback')),
            ],
            options={
                'verbose_name': 'Выполненые заявки',
                'db_table': 'zayavki_done',
            },
        ),
    ]