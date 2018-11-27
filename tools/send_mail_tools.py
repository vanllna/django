from users.models import *
import random
from pro.settings import EMAIL_FROM
from django.core.mail import send_mail

def get_random_code(code_length):
    #验证码 随机数据
    code_source = '1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
    code = ''
    for i in range(code_length):
        #创建验证码
        codestr = code_source[random.randrange(0,len(code_source)-1)]
        code += codestr
    return code


def send_mail_code(email,send_type):
    #创建邮箱验证码对象  保存数据库 用于数据对比
    code = get_random_code(8)
    e = EmailVerifyCode()
    e.email = email
    e.send_type = send_type
    e.code = code
    e.save()

    #发邮件功能
    send_title = ''
    send_body = ''
    if send_type == 1:
        send_title = 'welcone register'
        send_body = 'please click url active : \n http://127.0.0.1:8000/users/users_active/'+code
        send_mail(send_title,send_body,EMAIL_FROM,[email])

    if send_type == 2:
        send_title = 'password reset'
        send_body = 'please click url reset you password: \n http://127.0.0.1:8000/users/users_reset/'+code
        send_mail(send_title,send_body,EMAIL_FROM,[email])
    if send_type == 3:
        send_title = 'updateemail'
        send_body = 'please copy you code : \n'+code
        send_mail(send_title,send_body,EMAIL_FROM,[email])