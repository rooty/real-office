# -*- coding: utf-8 -*-
from os.path import join, dirname
from django.conf import settings
from django.conf.urls.defaults import *
from .views import MessagesList, viewmessages, new_message, viewmessage, \
                    reply_message, view_projects, new_project, view_project, view_home, \
                    project_add_task, task_edit, edit_project, view_contacts,new_contact, \
                    view_contact, edit_contact, del_contact, del_message, view_adverts, \
                    view_advert, edit_advert

urlpatterns = patterns('',
    #url(r'^$', viewmessages,name='view_messages'),
    url(r'^$', view_home, name='view_home'),
    url(r'^messages/folder/(?P<folder_id>\d+)/$', viewmessages,name='view_messages'),
    url(r'^messages/view/(?P<message_id>\d+)/$', viewmessage,name='view_message'),
    url(r'^messages/reply/(?P<message_id>\d+)/$', reply_message, name='reply_message'),
    url(r'^messages/del/(?P<message_id>\d+)/$', del_message, name='del_message'),
    url(r'^messages/new/$', new_message,name='new_messages'),
    url(r'^projects/$', view_projects,name='view_projects'),
    url(r'^project/new/$', new_project,name='new_project'),
    url(r'^project/view/(?P<project_id>\d+)/$', view_project,name='view_project'),
    url(r'^project/edit/(?P<project_id>\d+)/$', edit_project,name='edit_project'),
    url(r'^project/(?P<project_id>\d+)/addtask/$', project_add_task,name='project_add_task'),
    url(r'^task/(?P<task_id>\d+)/$', task_edit,name='task_edit'),
    url(r'^contacs/$', view_contacts,name='view_contacts'),
    url(r'^contacs/contacttype/(?P<type_id>\d+)/$', view_contacts,name='view_contacts'),
    url(r'^contacs/view/(?P<contact_id>\d+)/type/(?P<type_id>\d+)/$', view_contact,name='view_contact'),
    url(r'^contacs/edit/(?P<contact_id>\d+)/type/(?P<type_id>\d+)/$', edit_contact,name='edit_contact'),
    url(r'^contacs/del/(?P<contact_id>\d+)/type/(?P<type_id>\d+)/$', del_contact,name='del_contact'),
    url(r'^contacs/new/$', new_contact,name='new_contact'),
    url(r'^adverts/$', view_adverts,name='view_adverts'),
    url(r'^adverts/type/(?P<type_id>\d+)/$', view_adverts,name='view_adverts'),
    url(r'^advert/view/(?P<advert_id>\d+)/$', view_advert,name='view_advert'),
    url(r'^advert/edit/(?P<advert_id>\d+)/$', edit_advert,name='edit_advert'),
    #url(r'^messages/$', MessagesList.as_view(), name='view_messages'),
    #    (r'^news/$', list_detail.object_list, news_info)
    #    (r'^categories/(?P<name>[-\w]+)/$', cat_index),
    #    (r'^(?P<slug>[-\w]+)/$', full_news),
)
