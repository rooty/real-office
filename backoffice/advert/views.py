# -*- coding: utf-8 -*-
__author__ = '$USER'
from django.conf import settings
from django.shortcuts import render_to_response
from django.template import RequestContext, loader
from django.db.models.query_utils import Q
from django.http import HttpResponse, HttpResponseRedirect, Http404, HttpRequest, HttpResponseForbidden
import operator
import datetime
from simplepagination import paginate
from annoying.decorators import render_to
from registration.forms import RegistrationFormUniqueEmail
from django.forms.util import ErrorList
from django.contrib.auth.decorators import login_required
#from django.contrib import sitemaps
from django.core import serializers
from django.utils import simplejson
from forms import *
from models import Photo, ContactInfo, CityArea, Advert, Street, RealType, RealType2, Photo, Currency
from advert2.models import Advert2
from decimal import Decimal
from real.utils import convert2uah

def display_post(request):
    values = request.POST.items()
    values.sort()
    html = []
    for k, v in values:
        html.append('<tr><td>%s</td><td>%s</td></tr>' % (k, v))
    return HttpResponse('<table>%s</table>' % '\n'.join(html))
                            



def street(request):
    value = request.GET['query']
    city = request.GET['city']
    street_list = Street.objects.filter(name__icontains=value, cityid=city)
    new_list =[]
    data = []
    for o in street_list:
        new_list.append(o.name)
        data.append(str(o.id))
    response_dict = {}
    response_dict.update( {'query' : value, 'suggestions' : new_list , 'data': data })
    return HttpResponse(simplejson.dumps(response_dict) , mimetype='application/javascript')


def feeds_realtype2(request):
    """
    запрост поиска подтипов недвижимости
    
    """
    qstr = request.GET.get('id','')
    if qstr:
        qs = RealType2.objects.filter(parenttype=qstr)
    else:
        qs = []
    return HttpResponse(serializers.serialize("json", qs), mimetype="application/javascript")

class DivErrorList(ErrorList):

    def __unicode__(self):
        return self.as_divs()

    def as_divs(self):
        if not self: return u''
        ret = ''.join([u'<div class="error" style="color:#ff0000;">%s</div>' % e for e in self])
        return u'<div class="errorlist" style="color:#ff0000;">%s</div>' % ret

@render_to('novostroy.html')
@paginate(style='digg', per_page=10)
def search_advert2(request):

    request.session.set_expiry(0)
    if request.method == 'POST':
        form_data = request.POST
        request.session['form_data'] = request.POST
    elif request.method == 'GET':
        form_data = request.session.get('form_data',None)
    else:
        form_data = None
    if request.method == 'POST' or request.method == 'GET':
        searchform1 = SearchForm1(form_data)
        realtypeid = form_data.get('realtypeid', '')

     #   qresults = []

    qresults = Advert2.objects.all()
    context = {
        "object_list": qresults,
        "subtype":realtypeid,
#        "flat": qresults,
        'searchform1' : searchform1,
        'logform': RegistrationFormUniqueEmail,
        }
    return context
#@render_to_new(template)


@render_to('nedvijimost.html')
@paginate(style='digg', per_page=10)
def search_advert(request):
    request.session.set_expiry(0)
    if request.method == 'POST':
        form_data = request.POST
        request.session['form_data'] = request.POST
    elif request.method == 'GET':
        form_data = request.session.get('form_data',None)
    else:
        form_data = None

    if request.method == 'POST' or request.method == 'GET':
        searchform1 = SearchForm1(form_data)
        realtypeid = form_data.get('realtypeid', '')
        cityarea = form_data.get('cityarea', '')
        countryarea = form_data.get('countryarea', '')
        city = form_data.get('city', '')
        roomstype = form_data.get('roomstype', '')
        roomscount = form_data.get('roomscount','')
        #        flattype = form_data.get('flattype', '')
        housetype = form_data.get('housetype', '')
        square1 = form_data.get('square1', '')
        square2 = form_data.get('square2', '')
        floor1 = form_data.get('floor1', '')
        floor2 = form_data.get('floor2', '')
        floors1 = form_data.get('floors1', '')
        floors2 = form_data.get('floors2', '')
        flattype = form_data.get('flattype', '')
        housematerial = form_data.get('housematerial', '')
        cost1 = form_data.get('cost1', '')
        cost2 = form_data.get('cost2', '')
        currency = form_data.get('currency', '')
        usercurrency = form_data.get('usercurrency', '')
        landsize1 = form_data.get('landsize1', '')
        landsize2 = form_data.get('landsize2', '')
        #        roomscount = form_data.get('roomscount', '')
        for_object = form_data.get('for_object', '')
        for_m2 = form_data.get('for_m2', '')
        photoyes = form_data.get('photoyes', '')
        videoyes = form_data.get('videoyes', '')
        comisionyes = form_data.get('comisionyes', '')
        stateofrepair = form_data.get('stateofrepair', '')
        bussinesperiod = form_data.get('bussinesperiod', '')
        businesscenterclass = form_data.get('businesscenterclass', '')
        separateentrance = form_data.get('separateentrance', '')
        locationofproperty = form_data.get('locationofproperty', '')
        typeoffund = form_data.get('typeoffund', '')
        metro = form_data.get('metro', '')
        ceill_height = form_data.get('ceill_height', '')
        wc_count = form_data.get('wc_count', '')
        operationtype = form_data.get('operationtype', '')
        pricefor = form_data.get('pricefor','')

        #print "realtype=="+str(realtypeid)

        if pricefor and len(cost1)>0:
            k = str(convert2uah(int(cost1),int(usercurrency)))
        if pricefor and len(cost2)>0:
            n = str(convert2uah(int(cost2),int(usercurrency)))

        qset = (Q())

        if operationtype and int(operationtype) > 0:

            qset &= (Q(operationtype__id=operationtype))

        if countryarea and int(countryarea) > 0:
            qset &= (Q(city__area__id__in=countryarea))

        if cityarea and int(cityarea) > 0:
            qset &= (Q(cityarea__id=cityarea))

        if city and int(city) > 0:
            qset &= (Q(city__id=city))

        if roomstype:
            qset &= Q(roomstype__id=roomstype)

        if roomscount:
            if int(roomscount) > 0:
                qset &= Q(rooms=roomscount)

        if square1:
            qset &= Q(square__gte=square1)

        if square2:
            qset &= Q(square__lte=square2)

        if floor1:
            qset &= Q(floor__gte=floor1)

        if floor2:
            qset &= Q(floor__lte=floor2)

        if roomstype:
            qset &= Q(roomstype__id=roomstype)

        if housetype:
            qset &= Q(housetype__id=housetype)

        if housematerial:
            qset &= Q(housematerial__id=housematerial)

        if realtypeid:
            qset &= Q(realtype__subtype__id=realtypeid)
        #            subset = RealType.objects.all().filter(subtype__id=realtypeid)
        #
        #        if len(qset) and len(subset):


        if pricefor and  pricefor=='2' and len(cost1)>0 and len(cost2)>0:
            qset &= Q(cost__range=(Decimal(k),Decimal(n)))
        if pricefor and  pricefor=='1'and len(cost1)>0 and len(cost2)>0:
            qset &= Q(costforall__range=(Decimal(k),Decimal(n)))

        if pricefor and pricefor=='1':
            if len(cost1)>0 and len(cost2)==0:
                qset &= Q(costforall__gte=Decimal(k))
            if len(cost1)==0 and len(cost2)>0:
                qset &= Q(costforall__lte=Decimal(n))

        if pricefor and pricefor=='2':
            if len(cost1)>0 and len(cost2)==0:
                qset &= Q(cost__gte=Decimal(k))
            if len(cost1)==0 and len(cost2)>0:
                qset &= Q(cost__lte=Decimal(n))
            #print "pricefor=="+pricefor
        #print "qset  ===="+str(qset)

        if len(qset):
        #	    print qset
        #            qresults = Advert.objects.filter(qset)
            qresults = Advert.objects.all().filter(qset)
        else:
            qresults = []
    else:
        qresults = []
        searchform1 = SearchForm1(form_data)

    context = {
        "object_list": qresults,
        "subtype":realtypeid,
        "flat": qresults,
        'searchform1' : searchform1,
        'logform': RegistrationFormUniqueEmail,
        }
    return context

@paginate(style='digg', per_page=10)
def search(request):
    request.session.set_expiry(0)
    if request.method == 'POST':
        form_data = request.POST
        request.session['form_data'] = request.POST
    elif request.method == 'GET':
        form_data = request.session.get('form_data',None)
    else:
        form_data = None

    if request.method == 'POST' or request.method == 'GET':
    #    searchforem1 = SearchForm1(form_data)
        realtypeid = form_data.get('realtypeid', '')
    #print "main realid==" +str(realtypeid)
    if realtypeid==str(3):
      return  search_advert2(request)

    else:
      return  search_advert(request)




@render_to('home.html')
@paginate(style='digg', per_page=10)
def view_homepage(request):
    adv = Advert.objects.all()
    searchform1 = SearchForm1()
    return {
        'object_list':adv,
        'next': '/',
        'searchform1' : searchform1,
        'logform': RegistrationFormUniqueEmail,
    }


#@render_to('advert/adverts.html')
@render_to('nedvijimost.html')
@paginate(style='digg', per_page=10)
def view_all_advert(request):
    form_data = request.session.get('form_data',None)
    adv = Advert.objects.all()
    searchform1 = SearchForm1(form_data)
    return {
        'object_list':adv,
        'logform': RegistrationFormUniqueEmail,
        'searchform1' : searchform1,
    }


@render_to('nedvijimost_one.html')
def view_advert(request, advert_id):
#    form_data = request.session.get('form_data',None)
    if advert_id:
        flat = Advert.objects.get(pk=advert_id)
    else:
        flat = Advert.objects.all()[:1]

    mapaddr = flat.get_mapaddress()
#    searchform1 = SearchForm1(form_data)
    searchform1 = SearchForm1()
    return {
        'object_list':flat,
        'flat':flat,
        'mapaddr':mapaddr,
        'pagetitle': flat.title,
        'logform': RegistrationFormUniqueEmail,
        'searchform1' : searchform1,
    }

@render_to('nedvijimost_one.html')
def view_advert_by_slug(request, slug):
#    form_data = request.session.get('form_data',None)
    if slug:
        flat = Advert.objects.get(slug=slug)
    else:
        flat = Advert.objects.all()[:1]
    flat.viewcount += 1
    flat.save()
    
    mapaddr = flat.get_mapaddress()
#    searchform1 = SearchForm1(form_data)
    searchform1 = SearchForm1()
    fotos = Photo.objects.all().filter(advert=flat)
    subtype = flat.realtype.subtype.id
    usercurrency = Currency.objects.get(id=flat.usercurrency_id)
    return {
        'object_list':flat,
        'flat':flat,
        'subtype':str(subtype),
        'currency':usercurrency,
        'fotos':fotos,
        'mapaddr':mapaddr,
        'pagetitle':flat.get_slug_name(),
        'logform': RegistrationFormUniqueEmail,
        'searchform1' : searchform1,
    }

@render_to('novostroy_one.html')
def view_novostroy_by_slug(request, slug):
    from advert2.models import Photo,Apartment
    if slug:
        novostroy = Advert2.objects.get(slug=slug)
    else:
        novostroy = Adver2t.objects.all()[:1]
    novostroy.viewcount += 1
    novostroy.save()

    mapaddr = novostroy.get_mapaddress()
    searchform1 = SearchForm1()
    fotos = Photo.objects.all().filter(advert=novostroy)
    apartments_1 = Apartment.objects.all().filter(advert=novostroy,rooms=1)
    apartments_2 = Apartment.objects.all().filter(advert=novostroy,rooms=2)
    apartments_3 = Apartment.objects.all().filter(advert=novostroy,rooms=3)
    apartments_4 = Apartment.objects.all().filter(advert=novostroy,rooms__gte=4)
    usercurrency = Currency.objects.get(id=novostroy.currency_id)
    realtype = novostroy.realtype.id
    return {
        'object_list_1':apartments_1,
        'object_list_2':apartments_2,
        'object_list_3':apartments_3,
        'object_list_4':apartments_4,
        'flat':novostroy,
        'subtype':str(realtype),
        'currency':usercurrency,
        'fotos':fotos,
        'mapaddr':mapaddr,
        'pagetitle':novostroy.get_slug_name(),
        'logform': RegistrationFormUniqueEmail,
        'searchform1' : searchform1,
        }


@login_required
@render_to('new_house.html')
def new_advert(request):
    if request.method == 'POST':
        advertform = AdvertForm(request.POST, request.FILES)
        contactform = ContactInfoForm(request.POST, request.FILES)
        if advertform.is_valid() and contactform.is_valid():
            newadvert = advertform.save(commit=False)
            newadvert.planning = newadvert.planning
            newadvert.poster = newadvert.poster
            newadvert.user = request.user
            newadvert.contact = contactform.save()
            newadvert.save()
            newadvert.save_m2m()
            return HttpResponseRedirect('/advert/thanks/')
    else:
        advertform = AdvertForm(
            initial = {'user':request.user},
            error_class=DivErrorList,
#            instance='advert_add',
        )
        contactform = ContactInfoForm(
            error_class=DivErrorList,
#            instance='contact_from',
        )
        
    return {
        'form': advertform,
        'contactform':contactform,
        'logform': RegistrationFormUniqueEmail,
    }


@login_required
#@render_to('new_house.html')
def delete_advert(request, advert_id):
    adv = Advert.objects.get(pk=advert_id)
    contact = ContactInfo.objects.get(pk=adv.contact.id)
    contact.delete()
    adv.delete()
    return HttpResponseRedirect('/advert/')

@login_required
#@render_to('new_house.html')
def update_advert(request, advert_id):
    adv = Advert.objects.get(pk=advert_id)
    adv.publication_date = datetime.datetime.now
    adv.save()
    adv.save_m2m()
    return HttpResponseRedirect('/advert/%s/' % advert_id)

@login_required
@render_to('edit_new_house.html')
def edit_advert(request, advert_id):
    #adv = Advert.objects.get(pk=advert_id,user=request.user)

    try:
        adv = Advert.objects.get(pk=advert_id,user=request.user)
    except Advert.DoesNotExist:
        raise Http404

    contact = ContactInfo.objects.get(pk=adv.contact.id)
    value = adv.realtype.subtype_id
    value = int(value)
    if value==1:
        advertform = AdvertForm(instance=adv,error_class=DivErrorList)
    if value==2:
        advertform = AdvertForm2(instance=adv,error_class=DivErrorList)

    contactform = ContactInfoForm(instance=contact,error_class=DivErrorList)
    advertform.countryarea = adv.city.area
    #print adv.city.area
    #print "countryarea"+str(advertform.countryarea)
    return {
        'form': advertform,
        'realsubtype':value,
        'advertid': advert_id,
        'contactform':contactform,
        'logform': RegistrationFormUniqueEmail,
        }

@login_required
@render_to('edit_new_house.html')
def edit_new_advert(request, advert_id):
    adv = Advert.objects.get(pk=advert_id)
    contact = ContactInfo.objects.get(pk=adv.contact.id)
    value = adv.realtype.subtype_id
    value = int(value)



    advertform = AdvertForm(
        initial = {'user':request.user},
        error_class=DivErrorList
    )
    contactform = ContactInfoForm(
        error_class=DivErrorList
    )
    return {
        'form': advertform,
        'contactform':contactform,
        'logform': RegistrationFormUniqueEmail,
        }


@render_to('advert/thanks.html')
def advertthanks(request):
    return {}



#@cached( trigger = { "signal" : ( signals.post_save, signals.post_delete ), "sender" : Advert  } )
#def get_latest_adverts():
#    return list(Advert.objects.all().order_by("-publication_date")[:5])
#class ProjectSitemap(Sitemap):
#    changefreq = "never"
#    priority = 0.5
#
#    def items(self):
#        return Advert.objects.all()[0:10]
#
#    def lastmod(self, obj):
#        return obj.modified
