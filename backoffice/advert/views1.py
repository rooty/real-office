# -*- coding: utf-8 -*-
__author__ = '$USER'
from django.conf import settings
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
from forms import AdvertForm, ContactInfoForm, SearchForm1
from models import Photo, ContactInfo, CityArea, Advert, Street, RealType, RealType2, Photo, Currency
from decimal import Decimal
from dorohouse.utils import convert2uah

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


@render_to('nedvijimost.html')
@paginate(style='digg', per_page=10)
def search(request):
    """

    """
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
        realtypeid = request.POST.get('realtypeid', '')
        cityarea = request.POST.get('cityarea', '')
        countryarea = request.POST.get('countryarea', '')
        city = request.POST.get('city', '')
        roomstype = request.POST.get('roomstype', '')
        roomscount = request.POST.get('roomscount','')
#        flattype = request.POST.get('flattype', '')
        housetype = request.POST.get('housetype', '')
        square1 = request.POST.get('square1', '')
        square2 = request.POST.get('square2', '')
        floor1 = request.POST.get('floor1', '')
        floor2 = request.POST.get('floor2', '')
        floors1 = request.POST.get('floors1', '')
        floors2 = request.POST.get('floors2', '')
        flattype = request.POST.get('flattype', '')
        housematerial = request.POST.get('housematerial', '')
        cost1 = request.POST.get('cost1', '')
        cost2 = request.POST.get('cost2', '')
        currency = request.POST.get('currency', '')
        usercurrency = request.POST.get('usercurrency', '')
        landsize1 = request.POST.get('landsize1', '')
        landsize2 = request.POST.get('landsize2', '')
#        roomscount = request.POST.get('roomscount', '')
        for_object = request.POST.get('for_object', '')
        for_m2 = request.POST.get('for_m2', '')
        photoyes = request.POST.get('photoyes', '')
        videoyes = request.POST.get('videoyes', '')
        comisionyes = request.POST.get('comisionyes', '')
        stateofrepair = request.POST.get('stateofrepair', '')
        bussinesperiod = request.POST.get('bussinesperiod', '')
        businesscenterclass = request.POST.get('businesscenterclass', '')
        separateentrance = request.POST.get('separateentrance', '')
        locationofproperty = request.POST.get('locationofproperty', '')
        typeoffund = request.POST.get('typeoffund', '')
        metro = request.POST.get('metro', '')
        ceill_height = request.POST.get('ceill_height', '')
        wc_count = request.POST.get('wc_count', '')
        operationtype = request.POST.get('operationtype', '')
        pricefor = request.POST.get('pricefor','')
        
        if pricefor and len(cost1)>0:
            k = str(convert2uah(int(cost1),int(usercurrency)))
        if pricefor and len(cost2)>0:
            n = str(convert2uah(int(cost2),int(usercurrency)))
        
        qset = (Q())

        if operationtype and int(operationtype) > 0:
#        if operationtype:
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
    qresults = Advert.objects.all()
    return {
        "object_list": qresults,
        "flat": qresults,
        'searchform1' : searchform1,
        'logform': RegistrationFormUniqueEmail,
    }

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
def vew_advert_by_slug(request, slug):
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
    subtype = flat.realtype.subtype
    usercurrency = Currency.objects.get(id=flat.usercurrency_id)
    return {
        'object_list':flat,
        'flat':flat,
        'subtype':subtype,
        'currency':usercurrency,
        'fotos':fotos,
        'mapaddr':mapaddr,
        'pagetitle':flat.get_slug_name(),
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
@render_to('edit_house1.html')
def edit_advert(request, advert_id):
    adv = Advert.objects.get(pk=advert_id)
    contact = ContactInfo.objects.get(pk=adv.contact.id)
    if request.method == 'POST':
        advertform = AdvertForm(request.POST, request.FILES, instance=adv)
        contactform = ContactInfoForm(request.POST, request.FILES, instance=contact)
        if advertform.is_valid() and contactform.is_valid():
            newadvert = advertform.save(commit=False)
            newadvert.planning = unicode(newadvert.planning)
            newadvert.poster = unicode(newadvert.poster)
            #realtypeid = request.POST['realtype']
            realtypeid = 2
            newadvert.realtype = RealType.objects.get(pk=realtypeid) 
            streetid = request.POST['street']
            newadvert.street = Street.objects.get(pk=streetid)
            newadvert.save()
            newadvert.save_m2m()
            contact = contactform.save()
            contact.save()
            return HttpResponseRedirect('/advert/%s/' % advert_id)
            
    else:
	advertform = AdvertForm(instance=adv,error_class=DivErrorList)
	contactform = ContactInfoForm(instance=contact,error_class=DivErrorList)
    return {
            'form': advertform,
    	    'contactform':contactform,
            'logform': RegistrationFormUniqueEmail,
    }

#def edit(request, advert_id):
#    if request.method == 'POST':
#        form = AdvertForm(request.POST, request.FILES)
#        if form.is_valid():
#            newadvert = form.save()
#            newadvert.save()
#            return HttpResponseRedirect('/advert/thanks/')
#    else:
#        form = AdvertForm(Advert.objects.get(pk=advert_id))
#        return {
#            'form': form,
#            'logform': RegistrationFormUniqueEmail,
#        }


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
