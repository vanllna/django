from django import forms
from .models import *
import re

#ModelForm 用法
class UserAskForms(forms.ModelForm):
    class Meta:
        #利用models 的模型做验证
        model = UserAsk
        fields = ['name','phone','course']
        #全字段
        # fields = '__all__'
        #除了当前字段
        # exclude = ['add_time']
    def clean_phone(self):
        phone = self.cleaned_data['phone']
        com = re.compile('0?(13|14|15|17|18|19)[0-9]{9}')
        if com.match(phone):
            return phone
        else:
            raise forms.ValidationError('手机号码不正确')