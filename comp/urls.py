__author__ = 'Vicky Zhang'

from django.conf.urls import patterns, url
from comp import views

urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
                       url(r'^(?P<company_id>\d+)/$', views.detail, name='detail'),
                       url(r'^(?P<company>\w+)/review_summary/$', views.review_summary, name='review_summary')
                       )