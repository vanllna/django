# Generated by Django 2.1.3 on 2018-11-12 21:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20181109_1414'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 11, 12, 21, 20, 33, 518195), verbose_name='添加时间'),
        ),
    ]