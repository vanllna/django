import xadmin
from django.db import models
from datetime import datetime
from .models import *


class CityInfoXadmin(object):
    list_display = ['name','add_time']
    search_fields = ['name','add_time']
    list_filter = ['name','add_time']
    model_icon = 'fa fa-podcast'

class OrgInfoXadmin(object):
    list_display = ['image','name','course_num','study_num','address',
                    'desc','love_num','click_num','category','cityinfo','add_time']
    search_fields = ['image','name','course_num','study_num','address',
                    'desc','love_num','click_num','category','cityinfo','add_time']
    list_filter =  ['image','name','course_num','study_num','address',
                    'desc','love_num','click_num','category','cityinfo','add_time']
    style_fields = {'detail':'ueditor'}
    model_icon = 'fa fa-microchip'


class TeacherInfoXadmin(object):
    list_display = ['image','name','work_year','work_position','work_style','work_company',
                    'age','gender','love_num','click_num','add_time']
    search_fields = ['image','name','work_year','work_position','work_style','work_company',
                    'age','gender','love_num','click_num','add_time']
    list_filter = ['image','name','work_year','work_position','work_style','work_company',
                    'age','gender','love_num','click_num','add_time']
    model_icon = 'fa fa-free-code-camp'


xadmin.site.register(CityInfo,CityInfoXadmin)
xadmin.site.register(OrgInfo,OrgInfoXadmin)
xadmin.site.register(TeacherInfo,TeacherInfoXadmin)


