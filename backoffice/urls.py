import os
from os.path import join, dirname

from django.conf import settings
from django.conf.urls.defaults import patterns, include, url
from django.views.generic.base import TemplateView

from staticfiles.urls import static
media = os.path.join(
  os.path.dirname(__file__), 'media'
)

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', include('office.urls')),
    #url(r'^$', TemplateView.as_view(template_name = "base.html"), name="view_home_page"),
    url(r'^about/', TemplateView.as_view(template_name = "base.html"), name="about"),
    url(r'^contact/', TemplateView.as_view(template_name = "base.html"), name="contact"),
    url(r'^office/', include('office.urls')),
    url(r'^admin/', include(admin.site.urls)),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


if settings.DEBUG:
    urlpatterns += patterns(
        '',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve',{'document_root': settings.MEDIA_ROOT}),
        url(r'^media/(.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
        #        url(r'^static/(.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
        url(r'^admin-media/(.*)$', 'django.views.static.serve',{'document_root': join(dirname(admin.__file__), 'media')}),
    )
