# -*- coding: utf-8 -*-
from django import forms
from django.forms import ModelForm, widgets
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import forms as auth_forms
from django.utils.translation import ugettext_lazy as _
from .models import Message, Task, TaskState
from office.models import Project, OfficeContactInfo, ObjectCost, ObjectPayment, PaymentType, CostType
from advert.models import ComisionType, ContactType

class MessageForm(ModelForm):
    user_to = forms.ModelChoiceField(queryset=User.objects.filter(is_staff=True), empty_label=None)
    class Meta:

        model = Message
        fields = ('user_to', 'subject', 'body',)
        widgets = {
            #'user_to':widgets.Select(),
            'subject':widgets.TextInput({'class': 'input-xlarge', 'style': 'width:100%', 'placeholder': 'Тема сообщения'}),
            'body':widgets.Textarea({'class': 'input-xlarge', 'style': 'width:100%', 'placeholder': 'Сообщение'}),
        }

class MessageReplyForm(ModelForm):

    class Meta:
        model = Message
        fields = ('subject', 'body',)
        widgets = {
            'subject':widgets.TextInput({'class': 'input-xlarge', 'style': 'width:100%', 'placeholder': 'Тема сообщения'}),
            'body':widgets.Textarea({'class': 'input-xlarge', 'style': 'width:100%', 'placeholder': 'Сообщение'}),
        }

class TaskForm(ModelForm):
    state = forms.ModelChoiceField(queryset=TaskState.objects.all())
    worker = forms.ModelChoiceField(queryset=User.objects.filter(is_staff=True))
    class Meta:
        model = Task
        fields = ('title','description','state','worker','terminate')
        widgets = {
            'title':widgets.TextInput({'class': 'input-xlarge', 'style': 'width:100%', 'placeholder': 'Тема задачи'}),
            'description':widgets.Textarea({'class': 'input-xlarge', 'style': 'width:100%', 'placeholder': 'Описание задачи'}),
            'terminate':widgets.CheckboxInput({'style': 'width:100%', 'placeholder': 'Закончить задачу'}),
            }

class ProjectForm(ModelForm):

    class Meta:
        model = Project
        fields = ('title','description',)
        widgets = {
            'title':widgets.TextInput({'class': 'input-xlarge', 'style': 'width:100%', 'placeholder': 'Тема проекта'}),
            'description':widgets.Textarea({'class': 'input-xlarge', 'style': 'width:100%', 'placeholder': 'Описание проекта'}),
            }

class ContactInfoForm(ModelForm):
    fio = forms.CharField(widget=forms.TextInput(attrs = {"class":"input_et required"}))
    tel   = forms.CharField(widget=forms.TextInput(attrs = {"class":"input_et required"}))
    tel2   = forms.CharField(widget=forms.TextInput(attrs = {"class":"input_et"}),required=False)
    email = forms.EmailField(widget=forms.TextInput(attrs = {"class":"input_et required"}))
    skype = forms.CharField(widget=forms.TextInput(attrs = {"class":"input_et"}),required=False)
    #logocompany = forms.ImageField(required=False)
    logocompany = forms.ImageField()
    accounttype = forms.ModelChoiceField(queryset=ContactType.objects.all(),widget=forms.Select(attrs = {"class":"sel required"}))
    comision = forms.ModelChoiceField(queryset=ComisionType.objects.all(),widget=forms.Select(attrs = {"class":"sel required"}))



    class Meta:
        model = OfficeContactInfo
        exclude = ('owner',)

class ObjectPaymentForm(ModelForm):
    payment = forms.ModelChoiceField(queryset=PaymentType.objects.all())

    class Meta:
        model = ObjectPayment
        exclude = ('advert',)
        widgets = {
            'description':widgets.TextInput({'class': 'input-xlarge', 'style': 'width:100%','placeholder': u'описание оплаты'}),
            'payment':widgets.Select({'class': 'input-xlarge', 'style': 'width:100%','placeholder': u'тип оплаты'}),
            'summa':widgets.TextInput({'class': 'input-xlarge', 'style': 'width:100%', 'placeholder': u'сумма оплаты'}),
            }

class ObjectCostForm(ModelForm):
    cost = forms.ModelChoiceField(queryset=CostType.objects.all())

    class Meta:
        model = ObjectCost
        exclude = ('advert',)
        widgets = {
            'description':widgets.TextInput({'class': 'input-xlarge', 'style': 'width:100%','placeholder': u'описание затрат'}),
            'cost':widgets.Select({'class': 'input-xlarge', 'style': 'width:100%','placeholder': u'тип затрат'}),
            'summa':widgets.TextInput({'class': 'input-xlarge', 'style': 'width:100%', 'placeholder': u'сумма затрат'}),
            }
