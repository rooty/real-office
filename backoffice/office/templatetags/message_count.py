from django import template
from office.models import Message

register = template.Library()

@register.simple_tag(takes_context=True)
def pmcount(context):
    user = context['user']
    all = Message.objects.filter(user_to=user).count()
    newpm = Message.objects.filter(user_to=user, delivery=False).count()
    ret = "%s/%s" % (newpm, all)
    return ret



