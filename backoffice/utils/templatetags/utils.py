from itertools import izip, chain, repeat
import re

from django.utils.safestring import mark_safe
from django.core.serializers import serialize
from django.db.models.query import QuerySet
from django.template import Library
from django.utils import simplejson
from django.utils.datastructures import SortedDict

from imagekit.models import ImageSpecFile
from staticfiles.templatetags.staticfiles import static

register = Library()

class_re = re.compile(r'(?<=class=["\'])(.*)(?=["\'])')


@register.filter
def add_class(value, css_class):
    string = unicode(value)
    match = class_re.search(string)
    if match:
        m = re.search(r'^%s$|^%s\s|\s%s\s|\s%s$' % (css_class, css_class,
                                                    css_class, css_class),
                      match.group(1))
        if not m:
            return mark_safe(class_re.sub(match.group(1) + " " + css_class,
                                          string))
    else:
        return mark_safe(string.replace('>', ' class="%s">' % css_class))
    return value


@register.filter
def jsonify(object):
    if isinstance(object, QuerySet):
        return serialize('json', object)
    return simplejson.dumps(object)


@register.simple_tag
def avatar(profile, image='thumb'):
    style = "avatar_%s" % image
    default_image = static("images/%s.png" % style)
    avatar = getattr(profile, style, default_image)

    if isinstance(avatar, ImageSpecFile):
        try:
            return avatar.url
        except ValueError:
            return default_image
    else:
        return avatar


@register.simple_tag(takes_context=True)
def form_errors(context):
    form = context['form']
    return simplejson.dumps(__sort_errors(form))


def __sort_errors(form):
    """ Sort form errors into ordered dictionary """
    errors = SortedDict()
    for field in form:
        if not field.is_hidden and field.errors:
            errors[field.name] = field.errors
    return errors


@register.simple_tag
def current(request, pattern, style='active'):
    import re

    if re.search(pattern, request.path):
        return style
    return ''


@register.filter
def grouper(iterable, n, padvalue=None):
    "grouper(3, 'abcdefg', 'x') -> ('a','b','c'), ('d','e','f'), ('g','x','x')"
    return izip(*[chain(iterable, repeat(padvalue, n - 1))] * n)
