# Generated by Django 2.1.3 on 2018-11-24 14:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_auto_20181124_1435'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 11, 24, 14, 50, 27, 610981), verbose_name='添加时间'),
        ),
    ]
