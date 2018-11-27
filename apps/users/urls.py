from django.conf.urls import url
from . import views

app_name = 'users'
urlpatterns = [
    url(r'users/$',views.Home,name='index'),
    url(r'usersclass/$',views.IndexHone.as_view(),name='indexcclass'),
    url(r'register/$',views.register,name='register'),
    url(r'login/$',views.userlogin,name='login'),
    url(r'users_active/(\w+)/$',views.users_active,name='users_active'),
    url(r'users_reset/(\w+)/$',views.users_reset,name='users_reset'),
    url(r'forgetpwd/$',views.forgetpwd,name='forgetpwd'),
    url(r'userinfo/$',views.UserInfo,name='userinfo'),
    url(r'userchangeimage/$',views.UserChangeImageForm,name='userchangeimage'),
    url(r'userchangeinfo/$',views.UserChangeInfo,name='userchangeinfo'),
    url(r'updateemail/$',views.UpdateEmail,name='updateemail'),
    url(r'emailcode/$',views.EmailCode,name='emailcode'),
    url(r'resetemail/$',views.ResetEmail,name='resetemail'),
    url(r'usercoures/$',views.UserCoures,name='usercoures'),
    url(r'userlove/$',views.UserLoveOrg,name='userlove'),
]



