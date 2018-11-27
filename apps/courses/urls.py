from django.conf.urls import url
from . import views

app_name = 'coures'

urlpatterns = [
    url(r'coures/$',views.CouresInfo ,name='couresinfo'),
    url(r'couresdetail/(\d+)/$',views.CouresDetail ,name='couresdetail'),
    url(r'couresvideo/(\d+)/$',views.CouresVideo ,name='couresvideo'),
    url(r'courescomment/$',views.CouresComment ,name='courescomment'),
]