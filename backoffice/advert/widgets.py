# -*- coding: utf-8 -*-
from django_widgets import Widget
from models import Advert
from registration.forms import RegistrationFormUniqueEmail
from django.shortcuts import render_to_response

class HelloWorld(Widget):
    def render(self, context, value=None, options=None):
        return u'Hello world!'


class Top10Adverts(Widget):
    template = 'advert/top10.html'

    def get_context(self, value, options):
        """
        Top10Adverts.get_context описание
        """
        return {
#            'adv': Advert.objects.all().order_by("-publication_date")[:10]
            'adv': Advert.objects.all()[:10]
        }

class LoginForm(Widget):
    template = 'registration/loginform.html'
    logform =  RegistrationFormUniqueEmail

    def render(self, context, value=None, options=None):
#        return {'form': RegistrationFormUniqueEmail}
	return render_to_response('registration/loginform.html', {'logform': RegistrationFormUniqueEmail})
#
#    def get_context(self, value, options):
#        return {'form': RegistrationFormUniqueEmail}

#    def get_context(self, value, options):
#        return {
#    	    'form': RegistrationFormUniqueEmail,
#    	    'name' : 'registration_register',
#        }