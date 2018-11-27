# Generated by Django 2.1.3 on 2018-11-06 16:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserAsk',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='姓名')),
                ('phone', models.CharField(max_length=100, verbose_name='手机')),
                ('course', models.CharField(max_length=30, verbose_name='课程名')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='咨询时间')),
            ],
            options={
                'verbose_name': '咨询信息',
                'verbose_name_plural': '咨询信息',
            },
        ),
        migrations.CreateModel(
            name='UserComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_content', models.CharField(max_length=200, verbose_name='评论内容')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='学习时间')),
            ],
            options={
                'verbose_name': '评论信息',
                'verbose_name_plural': '评论信息',
            },
        ),
        migrations.CreateModel(
            name='UserCourse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='学习时间')),
            ],
            options={
                'verbose_name': '用户学习课程信息',
                'verbose_name_plural': '用户学习课程信息',
            },
        ),
        migrations.CreateModel(
            name='UserLove',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('love_id', models.IntegerField(verbose_name='收藏ID')),
                ('love_type', models.IntegerField(choices=[(1, 'org'), (2, 'course'), (3, 'teacher')], verbose_name='收藏类别')),
                ('love_status', models.BooleanField(default=False, verbose_name='收藏状态')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='收藏时间')),
            ],
            options={
                'verbose_name': '收藏信息',
                'verbose_name_plural': '收藏信息',
            },
        ),
        migrations.CreateModel(
            name='UserMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message_man', models.IntegerField(default=0, verbose_name='消息用户')),
                ('message_content', models.CharField(max_length=200, verbose_name='消息内容')),
                ('message_status', models.BooleanField(default=False, verbose_name='消息状态')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='学习时间')),
            ],
            options={
                'verbose_name': '消息信息',
                'verbose_name_plural': '消息信息',
            },
        ),
    ]
