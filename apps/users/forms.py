from django import forms
from captcha.fields import CaptchaField
from .models import *

class UserRegisterForm(forms.Form):
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True,min_length=3,max_length=10,error_messages={
        'required':'你输入的不正确',
        'min_length':'必须超过三个字符',
        'max_length':'必须小于10个字符'
    })
    captcha = CaptchaField()


class UserLoginForm(forms.Form):
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True,min_length=3,max_length=10,error_messages={
        'required':'你输入的不正确',
        'min_length':'必须超过三个字符',
        'max_length':'必须小于10个字符'
    })



class ForgetPwd(forms.Form):
    email = forms.EmailField(required=True)
    captcha = CaptchaField()


class UserResetForm(forms.Form):
    password = forms.CharField(required=True,min_length=3,max_length=10,error_messages={
        'required':'你输入的不正确',
        'min_length':'必须超过三个字符',
        'max_length':'必须小于10个字符'
    })
    password1 = forms.CharField(required=True,min_length=3,max_length=10,error_messages={
        'required':'你输入的不正确',
        'min_length':'必须超过三个字符',
        'max_length':'必须小于10个字符'
    })


class UserChangeImageForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields= ['image']

class UserChangeInfoForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['nick_name','tel']

class UserChangeEmailForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['email']


class UserResetEmailForm(forms.ModelForm):
    class Meta:
        model = EmailVerifyCode
        fields = ['email','code']

