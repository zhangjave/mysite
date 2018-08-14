from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^index/$', views.index, name='index'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.detail,name='detail'),
    url(r'^full/$', views.full_list,  name='full_list'),
]
