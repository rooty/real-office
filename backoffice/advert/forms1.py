# -*- coding: utf-8 -*-
from django import forms
from models import *

class AdvertForm(forms.Form):
    title = forms.CharField(max_length=255, label=u'заголовок объявления')
    description = forms.CharField(widget=forms.Textarea, label=u'текст объявления')
#class AdvertForm(forms.Form):
#    realtype = forms.ModelChoiceField()
#    realtype2id = forms.ModelChoiceField()

#    def clean_message(self):
#	message = self.cleaned_data[message]
#	num_words = len(message.split())
#	if num_words < 4:
#	    raise forms.ValidationError("Слишком мало слов")
#	return message




