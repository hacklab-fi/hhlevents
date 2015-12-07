# -*- coding: UTF-8 -*-
from django.conf import settings
from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from .views import RegView, RegOKView

urlpatterns = patterns('',
    url(r'^ok/$', TemplateView.as_view(template_name='hhlregistrations/register_ok.html'), name='regok_generic'),
    url(r'^(?P<event_id>[0-9a-f-]+)/$', RegView.as_view(), name='register'),
)