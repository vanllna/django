from django.contrib import admin
from django.urls import path,include
import xadmin

urlpatterns = [
    # path(r'^admin/', admin.site.urls),
    path(r'xadmin/', xadmin.site.urls),
    path(r'captcha/', include('captcha.urls')),
    path(r'ueditor/', include('DjangoUeditor.urls')),
    path(r'users/', include('users.urls' ,namespace='users')),
    path(r'courses/', include('courses.urls',namespace='coures' )),
    path(r'orgs/', include('orgs.urls' ,namespace='orgs')),
    path(r'operations/', include('operations.urls',namespace='operations')),
]

'''设置全局的 400 500 错误页面'''
handler404 = 'users.views.error_404'
handler500 = 'users.views.error_500'

