from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime

# Create your models here.
class UserProfile(AbstractUser):
    # username = models.CharField(max_length=200,verbose_name='用户姓名')
    image = models.ImageField(upload_to='user/',max_length=200,verbose_name='头像',blank=True)
    nick_name = models.CharField(max_length=200,verbose_name='昵称',blank=True)
    birthday = models.DateTimeField(verbose_name='生日',blank=True,null=True)
    gender = models.CharField(verbose_name='性别',choices=(('girl','女'),('boy','男')),default='girl',max_length=20)
    tel = models.CharField(max_length=11,verbose_name='手机')
    address = models.CharField(max_length=100,verbose_name='地址',blank=True)
    email = models.EmailField()
    add_time = models.DateTimeField(default=datetime.now(),verbose_name='添加时间')
    is_start = models.BooleanField(default=False,verbose_name='是否激活')

    def __str__(self):
        return self.username

    def get_mes_count(self):
        from operations.models import UserMessage
        #获取未读消息的总数
        messagecount = UserMessage.objects.filter(message_man=self.id,message_status=False).count()
        return messagecount

    class Meta:
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name

class Banner(models.Model):
    image = models.ImageField(upload_to='banner/',verbose_name='广告图',max_length=200)
    url = models.URLField(default='https://www.baidu.com',verbose_name='链接',max_length=200)
    add_time = models.DateTimeField(default=datetime.now,verbose_name='添加时间',max_length=200)

    def __str__(self):
        return str(self.image)

    class Meta:
        verbose_name = '广告信息'
        verbose_name_plural = verbose_name

class EmailVerifyCode(models.Model):
    code = models.CharField(max_length=200,verbose_name='邮箱验证码')
    email = models.EmailField(verbose_name='验证邮箱')
    send_type = models.IntegerField(choices=((1,'register'),(2,'forget'),(3,'change')),verbose_name='验证码类型')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间', max_length=200)

    def __str__(self):
        return self.code

    class Meta:
        verbose_name = '邮箱验证'
        verbose_name_plural = verbose_name


