# -*- coding: utf-8 -*-
import datetime
import string

from django.contrib.auth.models import User
from django.db import models
from django.db.models import signals

from PIL import Image
from imagekit.models import ImageSpec
from imagekit.processors import resize, Adjust

from advert.models import Advert, ContactType, ComisionType


class MessageFolder(models.Model):
    name = models.CharField(max_length=128)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = "папка сообщения"
        verbose_name_plural = "папки сообщений"

# TODO: система сообщений
class Message(models.Model):
    user_from = models.ForeignKey(User, related_name='user_from_message', verbose_name=u'от кого')
    user_to = models.ForeignKey(User, related_name='user_to_message', verbose_name=u'кому')
    subject = models.CharField(max_length=128,verbose_name=u'тема сообщения')
    body = models.TextField(verbose_name=u'текст сообщения')
    #folder = models.ForeignKey(MessageFolder,verbose_name=u'папка')
    created = models.DateTimeField(auto_now_add=True)
    delivery = models.BooleanField(verbose_name=u'доставленно', default=False)
    readed = models.BooleanField(verbose_name=u'прочитанно', default=False)

    def __unicode__(self):
        return self.subject

    class Meta:
        ordering = ['-created']
        verbose_name = "сообщение"
        verbose_name_plural = "сообщения"

class Project(models.Model):
    title = models.CharField(max_length=128, verbose_name=u'имя проекта')
    description = models.TextField(verbose_name=u'описание проекта', default='')
    owner = models.ForeignKey(User, verbose_name=u'управляющий')
    date_start = models.DateField(verbose_name=u'дата начала',default=datetime.datetime.now())
    date_end = models.DateField(verbose_name=u'дата окончания',default=datetime.datetime.now())
    percenttask = models.IntegerField(verbose_name=u'процент выполнения', default=0, editable=False)


    def __unicode__(self):
        return self.title

    def is_expired(self):
        if datetime.date.today() > self.date_end:
            return True
        else:
            return False

    def get_tasks_worker(self):
        ss = []
        tasks = Task.objects.filter(project=self)
        for task in tasks:
            uu = task.worker
            ss.append(uu.username)

        return string.join(ss, ', ')

    class Meta:
        ordering = ['-date_start']
        verbose_name = "проект"
        verbose_name_plural = "проекты"

class TaskState(models.Model):
    name = models.CharField(max_length=128, verbose_name=u'состояние задачи')

    class Meta:
        verbose_name = "состояние задачи"
        verbose_name_plural = "состояния задач"

    def __unicode__(self):
        return self.name


class Task(models.Model):
    title = models.CharField(max_length=128, verbose_name=u'название задачи')
    description = models.TextField(verbose_name=u'описание задачи', default='')
    project = models.ForeignKey(Project, verbose_name=u'проект')
    priority = models.IntegerField(verbose_name=u'приоритет', default=0)
    created = models.DateTimeField(auto_now_add=True)
    date_end = models.DateField(verbose_name=u'дата окончания',default=datetime.datetime.now())
    state = models.ForeignKey(TaskState, verbose_name=u'состояние задачи')
    #assignedto = models.ManyToManyField(User, related_name='taskasigneduser', verbose_name=u'исполнители задачи')
    worker = models.ForeignKey(User, verbose_name=u'рабочий', null=True)
    terminate = models.BooleanField(verbose_name=u'задача окончена', default=False)

    def __unicode__(self):
        return self.title


    class Meta:
        ordering = ['-created']
        verbose_name = "задача"
        verbose_name_plural = "задачи"


class OfficeContactInfo(models.Model):
    owner = models.ForeignKey(User)
    fio = models.CharField(max_length=128, verbose_name=u'Контактное лицо')
    tel = models.CharField(max_length=128, verbose_name=u'Телефон')
    tel2 = models.CharField(max_length=128, verbose_name=u'телефон2', blank=True)
    email = models.EmailField(max_length=128, verbose_name=u'E-mail')
    skype = models.CharField(max_length=128, blank=True)
    logocompany = models.ImageField(upload_to='people/', blank=True,verbose_name=u'Логотип компании')
    accounttype = models.ForeignKey(ContactType,verbose_name=u'Тип аккаунта')
    comision = models.ForeignKey(ComisionType, verbose_name=u'Коммисия')
    comissionvalue = models.DecimalField(max_digits=20,decimal_places=2,verbose_name=u'Размер комиссии', blank=True, default=0)
    logocompany_medium = ImageSpec([Adjust(contrast=1.2, sharpness=1.1),
                                    resize.Fit(235, )], image_field='logocompany',
        format='JPEG', options={'quality': 90})
    logocompany_small = ImageSpec([Adjust(contrast=1.2, sharpness=1.1),
                                   resize.Fit(50, 50)], image_field='logocompany',
        format='JPEG', options={'quality': 90})

    def __unicode__(self):
        return self.fio

    class Meta:
        verbose_name = u'информация о пользователе'
        verbose_name_plural = u'информация о пользователях'


class PaymentType(models.Model):
    name = models.CharField(verbose_name=u'тип оплаты', max_length=255)

    class Meta:
        verbose_name = "тип оплаты"
        verbose_name_plural = "тип оплаты"

    def __unicode__(self):
        return self.name

class CostType(models.Model):
    name = models.CharField(verbose_name=u'тип затрат', max_length=255)

    class Meta:
        verbose_name = "тип затрат"
        verbose_name_plural = "тип затрат"

    def __unicode__(self):
        return self.name


class ObjectPayment(models.Model):
    advert = models.ForeignKey(Advert)
    payment = models.ForeignKey(PaymentType,verbose_name=u'тип оплаты')
    description = models.TextField(verbose_name=u'описание оплаты')
    summa = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=u'сумма оплаты')

    class Meta:
        verbose_name = "оплата за объект"
        verbose_name_plural = "оплаты за объект"

    def __unicode__(self):
        return u"%s за %s" % (self.description, self.advert)

class ObjectCost(models.Model):
    advert = models.ForeignKey(Advert)
    cost = models.ForeignKey(CostType,verbose_name=u'тип затрат')
    description = models.TextField(verbose_name=u'описание затрат')
    summa = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=u'сумма затрат')

    class Meta:
        verbose_name = "затрата на объект"
        verbose_name_plural = "затраты за объекты"

    def __unicode__(self):
        return u"%s за %s" % (self.description, self.advert)


def count_payment_on_save(sender, instance, created, **kwargs):
    advert = instance.advert
    payments = ObjectPayment.objects.filter(advert=advert)
    summ1 = 0
    for payment in payments:
        summ1 += float(payment.summa)
    costs = ObjectCost.objects.filter(advert=advert)
    summ2 = 0
    for cost in costs:
        summ2 += float(cost.summa)
    advert.price2go = float(summ1 - summ2)
    advert.save()


def count_costs_on_save(sender, instance, created, **kwargs):
    advert = instance.advert
    payments = ObjectPayment.objects.filter(advert=advert)
    summ1 = 0
    for payment in payments:
        summ1 += float(payment.summa)
    costs = ObjectCost.objects.filter(advert=advert)
    summ2 = 0
    for cost in costs:
        summ2 += float(cost.summa)
    advert.price2go = float(summ1 - summ2)
    advert.save()


def count_percent_on_save(sender, instance, created, **kwargs):
    """
    расчет процента выполнения задачи
    """
    project = instance.project
    all = Task.objects.filter(project=project).count()
    term = Task.objects.filter(project=project,terminate=True).count()
    if all and term:
        project.percenttask = int(float(float(term)*100)/float(all))
    else:
        project.percenttask = 0
    project.save()


signals.post_save.connect(count_payment_on_save, sender=ObjectPayment, dispatch_uid='adverts.ObjectPayment')
signals.post_save.connect(count_costs_on_save, sender=ObjectCost, dispatch_uid='adverts.ObjectCost')
signals.post_save.connect(count_percent_on_save, sender=Task, dispatch_uid='projects.Task')
