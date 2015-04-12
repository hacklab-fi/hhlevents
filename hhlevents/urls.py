# -*- coding: UTF-8 -*-
from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import TemplateView

# Which packages need JS localizations
js_info_dict = {
    'packages': ('django.conf','django.contrib.admin',),
}


urlpatterns = patterns('',

    url(r'^$', TemplateView.as_view(template_name='base.html'), name='home'),

    url(r'^calendar/', include('happenings.urls', namespace='calendar')),
    url(r'^register/', include('hhlregistrations.urls', namespace='registrations')),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^jsi18n', 'django.views.i18n.javascript_catalog', js_info_dict),
    url(r'^i18n/', include('django.conf.urls.i18n')),

) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
