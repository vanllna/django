from django.conf.urls import url
from . import views

app_name = 'operations'

urlpatterns = [
    url(r'user_ask/$',views.user_ask,name='user_ask'),
    url(r'user_love/$',views.user_love,name='user_love'),
    url(r'user_dellove/$',views.user_dellove,name='user_dellove'),
]