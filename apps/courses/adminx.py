import xadmin
from .models import *


class CourseInfoXadmin(object):
    lsit_display = ['name','study_time','study_num','level','love_num','click_num',
                    'category','orgsinfo','teacherinfo']
    list_filter = ['name','study_time','study_num','level','love_num','click_num',
                    'category','orgsinfo','teacherinfo']
    search_fields = ['name','study_time','study_num','level','love_num','click_num',
                    'category','orgsinfo','teacherinfo']
    model_icon = 'fa fa-steam'

class LessonInfoXadmin(object):
    list_display = ['name','add_time','courseinfo']
    list_filter = ['name','add_time','courseinfo']
    search_fields = ['name','add_time','courseinfo']
    model_icon = 'fa fa-chrome'

class VideoInfoXadmin(object):
    list_display = ['name','study_time','url','add_time','lessoninfo']
    list_filter = ['name','study_time','url','add_time','lessoninfo']
    search_fields = ['name','study_time','url','add_time','lessoninfo']
    model_icon = 'fa fa-soundcloud'

class SourceInfoXadmin(object):
    list_display = ['name', 'down_load', 'courseinfo', 'add_time']
    list_filter = ['name', 'down_load', 'courseinfo', 'add_time']
    search_fields = ['name', 'down_load', 'courseinfo', 'add_time']
    model_icon = 'fa fa-rebel'

xadmin.site.register(CourseInfo,CourseInfoXadmin)
xadmin.site.register(LessonInfo,LessonInfoXadmin)
xadmin.site.register(VideoInfo,VideoInfoXadmin)
xadmin.site.register(SourceInfo,SourceInfoXadmin)

