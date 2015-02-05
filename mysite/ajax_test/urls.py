from django.conf.urls import patterns, url

from ajax_test import views

urlpatterns = patterns('',
  url(r'^$', views.index, name='index'),
  url(r'^async', views.async, name='async'),
)
