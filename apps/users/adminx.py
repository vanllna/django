import xadmin
from .models import *
from xadmin import views

#设置后台主题
class BaseXadminSetting(object):
    enable_themes = True
    use_bootswatch = True
#修改后台 title 和 footer 信息
class CommXadminSetting(object):
    site_title = '后台管理系统'
    site_footer = 'vanll'
    menu_style = 'accordion'
    # 后台导航 折叠处理

class BannerXadmin(object):
    list_display = ['image','url','add_time']
    search_fields = ['image','url']
    list_filter = ['image','url']
    model_icon = 'fa fa-ravelry'
    #修改后台图标


class EmailVerifyCodeXadmin(object):
    list_display = ['code','email','send_type','add_time']
    search_fields = ['code','email','send_type','add_time']
    list_filter = ['code','email','send_type','add_time']
    model_icon = 'fa fa-envelope-open'


xadmin.site.register(Banner,BannerXadmin)
xadmin.site.register(EmailVerifyCode,EmailVerifyCodeXadmin)
xadmin.site.register(views.BaseAdminView,BaseXadminSetting)
xadmin.site.register(views.CommAdminView,CommXadminSetting)




