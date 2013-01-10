# -*- coding: utf-8 -*-

import os
import uuid

from django.core.cache import cache
from django.core.urlresolvers import reverse
from django.utils import simplejson
from django.utils.hashcompat import md5_constructor
from django.utils.http import urlquote
from django.utils.functional import lazy
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth import REDIRECT_FIELD_NAME

import os
from PIL import Image
#from Pillow import *
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.conf import settings
from decimal import Decimal


def has_template_cache(fragment_name, *variables):
  args = md5_constructor(u':'.join([urlquote(var) for var in variables]))
  cache_key = 'template.cache.%s.%s' % (fragment_name, args.hexdigest())
  return cache_key in cache


def invalidate_template_cache(fragment_name, *variables):
  args = md5_constructor(u':'.join([urlquote(var) for var in variables]))
  cache_key = 'template.cache.%s.%s' % (fragment_name, args.hexdigest())
  cache.delete(cache_key)


def get_file_path(instance, filename):
    """
    Generate path for uploaded file base on class property ``upload_dir``
    """
    extension = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), extension)
    return os.path.join(instance.upload_dir, filename)

def form_errors_to_json(form):
    return simplejson.dumps({'success': False,
                             'errors': dict([(k, v[0])
                             for k, v in form.errors.items()])})

def is_staff_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME):
    """
    Decorator for views that checks that the user is staff, redirecting
    to the log-in page if necessary.
    Possible usage:
    @is_staff
    def view....

    urlpatterns = patterns('',
        (r'^databrowse/(.*)', is_staff(databrowse.site.root)),
    )
    """
    actual_decorator = user_passes_test(
        lambda u: u.is_staff,
        redirect_field_name=redirect_field_name
    )
    if function:
        return actual_decorator(function)
    return actual_decorator

def addwatermark(originimg, logoimg="logo_trans.png"):
    logoimg = os.path.join(settings.MEDIA_ROOT, logoimg)
    baseim = Image.open(originimg)
    logoim = Image.open(logoimg)  # transparent image
    baseim.paste(logoim, (baseim.size[0]-logoim.size[0],baseim.size[1]-logoim.size[1]), logoim)
    baseim.save(originimg)
    
def render_response(req, *args, **kwargs):
    kwargs['context_instance'] = RequestContext(req)
    return render_to_response(*args, **kwargs)

def get_thumbnail_url(image_url, size=150):
    thumbs_part = 'thumbs_' + str(size)
    image_url_parts = image_url.rsplit('/', 1)
    return image_url_parts[0] + '/' + thumbs_part + '/' + image_url_parts[1]

def get_thumbnail_path(image_path, size=150):
    thumbs_dir = 'thumbs_' + str(size)
    dirname, filename = os.path.split(image_path)
    dirname = os.path.join(dirname, thumbs_dir)
    if not os.path.exists(dirname):
        os.mkdir(dirname, 0755)
    return os.path.join(dirname, filename)

def create_thumbnail(image_path, size=150):
    thumb_path = get_thumbnail_path(image_path, size)
    delete_thumbnail(image_path, size)
    img = Image.open(image_path)
    img.thumbnail((size, size), Image.ANTIALIAS)
    img.save(thumb_path)

def delete_thumbnail(image_path, size=150):
    thumb_path = get_thumbnail_path(image_path, size)
    if os.path.exists(thumb_path):
        os.remove(thumb_path)

def convert2uah(val, curin):
    """
    вначале преобразовывает код валюты в коефициент, через масив
    потом пересчитываем
    """
    if curin > 2:
	return val
    if not val:
	val = 0
    if not curin:
	curin = 1
    coef = [8,1,10]
    retval = val * coef[curin - 1]
    retval  = str(retval)

    return Decimal(str(float(str(retval))))


reverse_lazy = lazy(reverse, str)

