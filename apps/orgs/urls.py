from django.conf.urls import url
from . import views

app_name = 'orgs'

urlpatterns = [
    url(r'orgs/$',views.OrgsList,name='orgs'),
    url(r'orgsdetail/(\d+)/$',views.OrgsDetail,name='orgsdetail'),

]