# -*- coding: utf-8 -*-
from django.conf.urls.defaults import *
from views import *
from ajax import *

urlpatterns = patterns('',
    (r'^$', view_all_advert),
    (r'^add/$', new_advert),
    (r'^add/new/$', send_form),
    (r'^add/new_edit/$', ajax_edit_advert),
    (r'^add/street/$', street),
    (r'^thanks/$', advertthanks),
    (r'^(?P<advert_id>\d+)/$', view_advert),
    (r'^(?P<slug>[-\w]+)/$', view_advert_by_slug),
    (r'^delete/(?P<advert_id>\d+)/$', delete_advert),
    (r'^advert/(?P<advert_id>\d+)/$', edit_advert),
    (r'^ajax/realtype/$', feeds_realtype2),
    (r'^ajax/categ/$', feeds_subcat),
)

