# Generated by Django 2.1.3 on 2018-11-24 14:35

import DjangoUeditor.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orgs', '0002_auto_20181112_2120'),
    ]

    operations = [
        migrations.AddField(
            model_name='orginfo',
            name='detail',
            field=DjangoUeditor.models.UEditorField(default='', verbose_name='机构详情'),
        ),
    ]
