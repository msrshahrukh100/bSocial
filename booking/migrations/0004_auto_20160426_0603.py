# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-04-26 06:03
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0003_users_last_login'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='users',
            table='users',
        ),
    ]