# -*- coding: utf-8 -*-
import uuid
import os
#from Pillow import *
from PIL import Image
from imagekit.models import ImageSpec
from imagekit.processors import resize, Adjust
from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.db.models.base import get_absolute_url
from sorl.thumbnail import ImageField
from autoslug import AutoSlugField
from decimal import Decimal
from django.utils.translation import ugettext_lazy as _
from backoffice.utils import convert2uah, addwatermark





class Watermark(object):
    def process(self, image):
        # Code for adding the watermark goes here.
        logoimg="logo_trans1.png"
        logoimg = os.path.join(settings.MEDIA_ROOT, logoimg)
        logoim = Image.open(logoimg)  # transparent image
        image.paste(logoim, (image.size[0]-logoim.size[0],image.size[1]-logoim.size[1]), logoim)
        return image


class ComisionType(models.Model):
    name = models.CharField(max_length=128, verbose_name=u'название комисии')

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u'тип комисии'
        verbose_name_plural = u'тип комисии'

        
class ContactType(models.Model):
    name = models.CharField(max_length=128, verbose_name=u'Действует как')

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u'тип контакта'
        verbose_name_plural = u'тип контакта'

class ContactInfo(models.Model):
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

class OperationType(models.Model):
    name = models.CharField(max_length=255,verbose_name=u'тип операции')

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u'тип операции с недвижимостью'
        verbose_name_plural = u'тип операций с недвижимостью'

class DoorType(models.Model):
    name = models.CharField(max_length=255,verbose_name=u'тип двери')

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u'тип двери'
        verbose_name_plural = u'тип дверей'


class RealType2(models.Model):
    name = models.CharField(max_length=255,verbose_name=u'Подтип недвижимости')

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u'подтип недвижимости'
        verbose_name_plural = u'подтипы недвижимости'


class RealType(models.Model):
    name = models.CharField(max_length=255,verbose_name=u'тип недвижимости')
    subtype = models.ForeignKey(RealType2)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u'тип недвижимости'
        verbose_name_plural = u'типы недвижимости'


class CountryArea(models.Model):
    name = models.CharField(max_length=255,verbose_name=u'область')

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u'область'
        verbose_name_plural = u'область'


class City(models.Model):
    name = models.CharField(max_length=255, verbose_name=u'Название города')
    area = models.ForeignKey(CountryArea, verbose_name=u'Область')
    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u'город'
        verbose_name_plural = u'города'

class CityArea(models.Model):
    name = models.CharField(max_length=255, verbose_name=u'Название района города')
    cityid = models.ForeignKey(City, verbose_name=u'Город')

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u'район города'
        verbose_name_plural = u'районы города'

class Metro(models.Model):
    name = models.CharField(max_length=255,verbose_name=u'станция метро')
    city = models.ForeignKey(City, verbose_name=u'Город')

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u'станция метро'
        verbose_name_plural = u'станции метро'



class Street(models.Model):
    name = models.CharField(max_length=255, verbose_name=u'Название улицы')
    cityid = models.ForeignKey(City, verbose_name=u'Город')

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u'улица'
        verbose_name_plural = u'улицы'


class FlatType(models.Model):
    name = models.CharField(max_length=255, verbose_name=u'Тип квартиры')

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u'тип квартиры'
        verbose_name_plural = u'типы квартир'

class HouseMaterial(models.Model):
    name = models.CharField(max_length=255, verbose_name=u'Тип материала здания')

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u'тип материала здания'
        verbose_name_plural = u'типы материалов зданий'

class HouseType(models.Model):
    name = models.CharField(max_length=255, verbose_name=u'Тип дома')
    realtype = models.ForeignKey(RealType , verbose_name=u'Тип недвижимости')

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u'тип дома'
        verbose_name_plural = u'типы дома'

class AdvOptions(models.Model):
    name = models.CharField(max_length=255)
    realtype = models.ForeignKey(RealType2)
    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u'удобства'
        verbose_name_plural = u'удобства'

class DopOptions(models.Model):
    name = models.CharField(max_length=255)
    realtype = models.ForeignKey(RealType2)
    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u'дополнительные опции'
        verbose_name_plural = u'дополнительные опции'



class AdvContact(models.Model):
    contact = models.CharField(max_length=255, verbose_name=u'Контактная информация')
    email = models.EmailField(verbose_name=u'Контактная почта')
    phone = models.CharField(max_length=32,verbose_name=u'Номер телефона')
    

    def __unicode__(self):
        return self.contact

    class Meta:
        verbose_name = u'контактная информация'
        verbose_name_plural = u'контактная информация'

class TrassaDirection(models.Model):
    name = models.CharField(max_length=255, verbose_name=u'Направлениы трассы от Киева')

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u'направление трассы от Киева'
        verbose_name_plural = u'направление трассы от Киева'

class LandPurpose(models.Model):
    name = models.CharField(max_length=255, verbose_name=u'назначение участка')

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u'название участка'
        verbose_name_plural = u'Назначения участков'

class Photo(models.Model):
    def get_file_path(self, filename):
        extension = filename.split('.')[-1]
        filename = "%s.%s" % (uuid.uuid4(), extension)
        return os.path.join("images", filename)

    advert = models.ForeignKey('Advert',blank=True, null=True)
    picture = models.ImageField(u'image', upload_to=get_file_path)
    picture_small = ImageSpec([Watermark(),Adjust(contrast=1.2, sharpness=1.1),
                               resize.Fit(50, 50)], image_field='picture',
        format='JPEG', options={'quality': 90})
    picture_medium = ImageSpec([Watermark(),Adjust(contrast=1.2, sharpness=1.1),
                                resize.Fit(800,600)], image_field='picture',
        format='JPEG', options={'quality': 90})

    def __unicode__(self):
        return self.advert.slug

    class Meta:

        verbose_name = u'Photo'
        verbose_name_plural = u'Photos'


class RoomType(models.Model):
    name  = models.CharField(max_length=128,verbose_name=u'Тип комнат')

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u'тип комнаты'
        verbose_name_plural = u'тип комнат'


class Currency(models.Model):
    name = models.CharField(max_length=128,verbose_name=u'Название валюты')

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u'название валюты'
        verbose_name_plural = u'название валют'


class FloorType(models.Model):
    name = models.CharField(max_length=128,verbose_name=u'тип полов')

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u'тип пола'
        verbose_name_plural = u'тип полов'


class StateOfRepair(models.Model):
    name = models.CharField(max_length=128,verbose_name=u'состояние ремонта')

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u'состояние ремонта'
        verbose_name_plural = u'состояние ремонта'


class TermAccommodation(models.Model):
    name = models.CharField(max_length=128,verbose_name=u'срок размещение')
    days = models.IntegerField(max_length=3,verbose_name=u'количество дней')

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u'срок размещение'
        verbose_name_plural = u'срок размещение'


class TypeOfFund(models.Model):
    name = models.CharField(max_length=128,verbose_name=u'тип фонда недвижимости')

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u'тип фонда недвижимости'
        verbose_name_plural = u'тип фонда недвижимости'


class LocationOfProperty(models.Model):
    name = models.CharField(max_length=128,verbose_name=u'расположение обьекта')

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u'расположение обьекта'
        verbose_name_plural = u'расположение обьекта'


class BusinessCenterClass(models.Model):
    name = models.CharField(max_length=128,verbose_name=u'класс бизнес центра')

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u'класс бизнес центра'
        verbose_name_plural = u'класс бизнес центра'


class SeparateEntrance(models.Model):
    name = models.CharField(max_length=128,verbose_name=u'отдельный вход')

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u'отдельный вход'
        verbose_name_plural = u'отдельный вход'


class ArendaBusinessPeriod(models.Model):
    name = models.CharField(max_length=128,verbose_name=u'аренда за период')
    period = models.IntegerField(null=False,verbose_name=u'количество дней',max_length=3)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u'аренда за период'
        verbose_name_plural = u'аренда за период'


class Advert(models.Model):
    def get_file_path(self, filename):
        extension = filename.split('.')[-1]
        filename = "%s.%s" % (uuid.uuid4(), extension)
        return os.path.join("images", filename)

    def get_slug_name(self):
        s = ''
        if self.street:
            s = self.street.name
        return "%s-%s-%s" % (self.realtype.subtype.name, self.city.name,s, )

    realtype = models.ForeignKey(RealType,verbose_name='Тип недвижимости')
#    realtype2 = models.ForeignKey(RealType2,verbose_name='Подтип недвижимости')
    operationtype = models.ForeignKey(OperationType, blank=True, null=True, default=0)
    city= models.ForeignKey(City,verbose_name=u'Город')
    cityarea = models.ForeignKey(CityArea,verbose_name=u'Район города',blank=True,null=True)
    street = models.ForeignKey(Street,verbose_name=u'Улица',blank=True,null=True)
    housenumber = models.CharField(max_length=32,verbose_name=u'номер дома',blank=True)
    flattypeid = models.ForeignKey(FlatType,verbose_name=u'Тип квартиры', null=True)
    housematerial = models.ForeignKey(HouseMaterial,verbose_name=u'Тип материала здания',blank=True,null=True)
    housetype = models.ForeignKey(HouseType,verbose_name=u'Тип дома',blank=True,null=True)
    rooms = models.IntegerField(verbose_name=u'количество комнат',default=0,blank=True)
    roomstype = models.ForeignKey(RoomType, verbose_name=u'Тип комнат')
    floor = models.IntegerField(verbose_name=u'этаж')
    floors = models.IntegerField(verbose_name=u'этажность')
    advoptions = models.ManyToManyField(AdvOptions, blank=True, related_name="Удобства")
    dopoptions = models.ManyToManyField(DopOptions, blank=True, related_name="Доп. опции")
    trassadirection = models.ForeignKey(TrassaDirection,verbose_name=u'Направление трассы из города',blank=True,null=True)
    landpurpose = models.ForeignKey(LandPurpose, verbose_name=u'назначение участка',blank=True,null=True)
    landsize = models.CharField(max_length=10,verbose_name=u'Размер участка',default='',blank=True,null=True)
    title = models.CharField(max_length=255, verbose_name=u'Заголовок статьи', default='', blank=True)
    desciption = models.TextField(verbose_name=u'Текст объявления', default='', blank=True)
    square = models.DecimalField(max_digits=20,decimal_places=2,verbose_name=u'Общая площадь',default=0)
    squarelife = models.DecimalField(max_digits=20,decimal_places=2,verbose_name=u'Жилая площадь',default=0,blank=True)
    kitchen = models.DecimalField(max_digits=20,decimal_places=2,verbose_name=u'Площадь кухни',null=True,blank=True,default=0)
#    home_deadline = models.DateField(u'срок сдачи дома',blank=True,default=datetime.datetime.now())
    home_deadline = models.CharField(u'срок сдачи дома',max_length=128, blank=True, null=True)
    free_from = models.CharField(u'свободно с даты',max_length=128, blank=True, null=True)
    free_to = models.CharField(u'свободно по',max_length=128, blank=True, null=True)
    floor_type = models.ForeignKey(FloorType,verbose_name=u'тип пола',blank=True,null=True)
    wc_count = models.IntegerField(verbose_name=u'количесво санузлов',blank=True,null=True)
    stateofrepair = models.ForeignKey(StateOfRepair,blank=True,null=True, verbose_name=u'состояние ремонта')
    ceill_height = models.DecimalField(verbose_name=u'высота потолков',max_digits=20,decimal_places=2,blank=True,null=True,    default=0)
    distance = models.CharField(verbose_name=u'дистанция от ',max_length=128,default='', blank=True, null=True)
    hotadv = models.BooleanField(default=False,verbose_name=u'Горячее предложение')
    created = models.DateTimeField(auto_now_add=True, editable=False)
    modified = models.DateTimeField(auto_now=True,editable=False)
    cost = models.DecimalField(max_digits=20,decimal_places=2,verbose_name=u'Цена в гривне за м2', blank=True)
    costforall = models.DecimalField(max_digits=20,decimal_places=0,verbose_name=u'Цена в гривне за объект', blank=True)
    usercost = models.DecimalField(max_digits=20,decimal_places=2,verbose_name=u'Цена продавца за м2')
    usercostforall = models.DecimalField(verbose_name=u'Цена продавца за объект', max_digits=20,decimal_places=0,)
    usercurrency = models.ForeignKey(Currency,verbose_name=u'Валюта продавца')
    publication_date = models.DateField(verbose_name=u'дата публикации', auto_now_add=True)
    viewcount = models.PositiveIntegerField(default=0,editable=False)
    metro = models.ForeignKey(Metro, verbose_name=u'Metro',blank=True,null=True)
    door = models.ForeignKey(DoorType,blank=True,null=True)
    term_accommodation = models.ForeignKey(TermAccommodation,blank=True,null=True)
    typeoffund = models.ForeignKey(TypeOfFund,blank=True,null=True)
    locationofproperty  = models.ForeignKey(LocationOfProperty,blank=True,null=True)
    businesscenterclass = models.ForeignKey(BusinessCenterClass,blank=True,null=True)
    separateentrance = models.ForeignKey(SeparateEntrance,blank=True,null=True)
    cabinetcount = models.CharField(verbose_name=u'количество кабинетов',max_length=256, blank=True)
    bussinesperiod = models.ForeignKey(ArendaBusinessPeriod,blank=True,null=True)
    planning = models.ImageField(upload_to=get_file_path, max_length=256, blank=True,verbose_name=u'фото планировки')
    poster = models.ImageField(verbose_name=u'Poster',upload_to=get_file_path,max_length=256, blank=True)
    video = models.FileField(verbose_name=u'Video',upload_to='video/',max_length=512, blank=True)
#    photos = models.ManyToManyField(Photo, blank=True, related_name="Фотографии объекта")
    contact = models.ForeignKey(ContactInfo)
    user = models.ForeignKey(User)
    torg = models.BooleanField(default=False,verbose_name=u'Торг')
    comissionvalue = models.DecimalField(max_digits=20,decimal_places=2,verbose_name=u'Размер комиссии', blank=True, default=0)
    slug = AutoSlugField(always_update=True, populate_from=get_slug_name, editable=False, unique=True)
    price2go = models.DecimalField(editable=False,decimal_places=2,max_digits=10,default=0.0)
    poster_small = ImageSpec([Watermark(),Adjust(contrast=1.2, sharpness=1.1),
                              resize.Fit(50, 50)], image_field='poster',
        format='JPEG', options={'quality': 90})
    poster_mainpage = ImageSpec([Watermark(),Adjust(contrast=1.2, sharpness=1.1),
                              resize.Fit(140,100)], image_field='poster',
        format='JPEG', options={'quality': 100})
    poster_medium = ImageSpec([Watermark(),Adjust(contrast=1.2, sharpness=1.1),
                               resize.Fit(800, 600)], image_field='poster',
        format='JPEG', options={'quality': 90})
    planning_small = ImageSpec([Watermark(),Adjust(contrast=1.2, sharpness=1.1),
                                resize.Fit(50, 50)], image_field='planning',
        format='JPEG', options={'quality': 90})
    planning_medium = ImageSpec([Watermark(),Adjust(contrast=1.2, sharpness=1.1),
                                 resize.Fit(800,600)], image_field='planning',
        format='JPEG', options={'quality': 90})

    def save(self, force_insert=False, force_update=False, using=None):

        if self.usercurrency.id ==1:
            a = self.usercost * 8
        if self.usercurrency.id ==2:
            a = self.usercost * 1
        if self.usercurrency.id ==3:
            a = self.usercost * 10
        a  = str(a)
        c = float(a) * float(self.square)
        self.cost = Decimal(str(float(a)))
        self.costforall = str(c)

        if self.usercurrency ==1:
            self.costforall = Decimal(self.usercostforall * 8)
        if self.usercurrency ==2:
            self.costforall = Decimal(self.usercostforall * 1)
        if self.usercurrency ==3:
            self.costforall = Decimal(self.usercostforall * 10)

        self.title = self.get_slug_name()
        super(Advert, self).save(force_insert, force_update, using)


    def get_absolute_url(self):
        return '/advert/%s/' % self.slug

    def get_mapaddress(self):
        s = ''
        if self.street:
            s = self.street.name
        return u'Украина, г. %s, %s %s' % (self.city.name, s, self.housenumber)

#    def getcomisionname(self):
#        return "%s" % (COMISION[self.contact.comision])

    def __unicode__(self):
        return '%d %s' % (self.id, self.title)

    def preview_image_url(self):
	image_path = Image.thumbnail(self.image, '60x60')
        image_path = image_path.replace('\\','/') # Windows-Fix
        return '<a href="'+ str(self.id) +'/"><img src="'+ str(image_path) +'"/></a>'
        
    preview_image_url.short_description = 'Thumbnail'
    preview_image_url.allow_tags = True
    
    class Meta:
        ordering = ['-publication_date']
        verbose_name = u'объявление'
        verbose_name_plural = u'объявления'


class PhotoAdvert(models.Model):
    photo  = models.ForeignKey(Photo,verbose_name=u'Фото')
    advert = models.ForeignKey(Advert,verbose_name=u'Объявление')

class ContactAdvert(models.Model):
    photo  = models.ForeignKey(ContactInfo,verbose_name=u'Фото')
    advert = models.ForeignKey(Advert,verbose_name=u'Объявление')

class UserCart(models.Model):
    cart_date = models.DateField(verbose_name=u'дата добавления в корзину', auto_now_add=True)
    user = models.ForeignKey(User,blank=True,null=True)
    advert = models.ForeignKey(Advert)
    session_key = models.TextField(editable=False,null=True, blank=True)
    def __unicode__(self):
        return u'корзина  %d от %s' % (self.id, self.cart_date)

    def get_absolute_url(self):
        return '/cabinet/usercart/%i/' % self.id

    class Meta:
        ordering = ['cart_date']
        verbose_name = u'корзина'
        verbose_name_plural = u'корзины'
