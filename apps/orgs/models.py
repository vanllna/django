from django.db import models
from datetime import datetime
from DjangoUeditor.models import UEditorField

# Create your models here.
class CityInfo(models.Model):
    name = models.CharField(max_length=20,verbose_name='城市名称')
    add_time = models.DateTimeField(default=datetime.now,verbose_name='添加时间')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '城市信息'
        verbose_name_plural = verbose_name


class OrgInfo(models.Model):
    image = models.ImageField(upload_to='org/',verbose_name='机构封面',max_length=200)
    name = models.CharField(max_length=200,verbose_name='机构名称')
    course_num = models.IntegerField(default=0,verbose_name='课程数')
    study_num = models.IntegerField(default=0,verbose_name='学习人数')
    address = models.CharField(max_length=200,verbose_name='机构地址')
    desc = models.CharField(max_length=200,verbose_name='机构简介')
    love_num = models.IntegerField(default=0,verbose_name='收藏数')
    click_num = models.IntegerField(default=0,verbose_name='访问量')
    category = models.CharField(choices=(('pxjg','培训机构'),('gx','高校'),('gr','个人')),max_length=200,verbose_name='机构类别')
    add_time = models.DateTimeField(default=datetime.now,verbose_name='添加时间')
    cityinfo = models.ForeignKey(CityInfo,verbose_name='所属城市',on_delete=models.CASCADE)
    detail = UEditorField(verbose_name='机构详情',
                          width=700,
                          height=600,
                          toolbars='full',
                          imagePath='ueditor/image/',
                          filePath='ueditor/files/',
                          upload_settings={'imageMaxSizing':102400},
                          default=''
                          )


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '机构信息'
        verbose_name_plural = verbose_name

class TeacherInfo(models.Model):
    image = models.ImageField(upload_to='teacher/',verbose_name='老师头像',max_length=200)
    name = models.CharField(max_length=200,verbose_name='老师姓名')
    work_year = models.IntegerField(default=0,verbose_name='工作年限')
    work_position = models.CharField(max_length=20,verbose_name='工作职业')
    work_style = models.CharField(max_length=20,verbose_name='教学特色')
    work_company = models.ForeignKey(OrgInfo,verbose_name='所属机构',on_delete=models.CASCADE)
    age = models.IntegerField(default=20,verbose_name='老师年龄')
    gender = models.CharField(max_length=20,verbose_name='性别',choices=(('girl','女'),('boy','男')))
    love_num = models.IntegerField(default=0,verbose_name='收藏数')
    click_num = models.IntegerField(default=0,verbose_name='访问量')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '老师信息'
        verbose_name_plural = verbose_name







