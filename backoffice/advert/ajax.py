# -*- coding: utf-8 -*-
from dajax.core import Dajax
from dajaxice.decorators import dajaxice_register
from django.template.loader import render_to_string
from django.views.decorators.csrf import csrf_protect
from django.http import HttpResponse, HttpResponseRedirect, Http404, HttpRequest, HttpResponseForbidden
from django.core.context_processors import csrf
from advert.forms import AdvertForm, ContactInfoForm, PhotoForm, PhotoFormSet
from django.utils import simplejson
from django.core import serializers
from django.forms.models import ModelMultipleChoiceField
from decimal import Decimal
import logging
from advert.forms import *
from advert.models import *
from django.contrib.auth.decorators import login_required

@login_required
def ajax_edit_advert(request):
    advert_id = request.POST['edit_id']
    adv = Advert.objects.get(pk=advert_id)

    value = adv.realtype.subtype_id
    #print 'advert_id=='+advert_id
    #print 'value=='+value
    value = str(value)



    if request.POST:
        if value=='1':
            advertform = AdvertFormEdit(request.POST, request.FILES, instance=adv)
            #print 'value1='+str(value)
            id = 'in1'

        if value=='2':
            advertform = AdvertForm2Edit(request.POST, request.FILES, instance=adv)
            #print 'value2='+str(value)
            id = 'in2'

        FormSet = PhotoFormSet2(request.POST, request.FILES)
        contactform = ContactInfoForm(request.POST, request.FILES)
        c={'form':advertform,'contactform':contactform,'formset':FormSet}
        c.update(csrf(request))



        if advertform.is_valid()  and contactform.is_valid() and  FormSet.is_valid():
            newadvert = advertform.save(commit=False)


            costall = request.POST['usercostforall']
            cost = request.POST['usercost']
            costall = str(costall)
            cost = str(cost)
            square = request.POST['square']
            ceill_height = request.POST['ceill_height']
            square = str(square)
            ceill_height = str(ceill_height)

            c = request.POST['comissionvalue']
            if c=='':
                c=0
            c = str(c)
            contactform.comissionvalue = Decimal(c)
            newadvert.usercost = Decimal(cost)
            newadvert.usercostforall = Decimal(costall)
            newadvert.square = Decimal(square)
            newadvert.ceill_height = Decimal(ceill_height)
            newadvert.user = request.user
            newadvert.contact = contactform.save(commit=False)

            newadvert.contact.logocompany = newadvert.contact.logocompany
            newadvert.contact = contactform.save()
            newadvert.save()
            #newadvert.advoptions.add(advertform.advoptions)
            advertform.save_m2m()

            instantces = FormSet.save(commit=False)
            for intance in instantces:
                intance.advert = newadvert
                intance.save()

            return HttpResponse(simplejson.dumps({'result': 'success'}))

        else:
            response = {}
            for k in advertform.errors:
                #print 'error advert==%s'% k
                response[k] = advertform.errors[k][0]

            for k in contactform.errors:
                #print 'error contact==%s'% k
                response[k] = contactform.errors[k][0]

            dict = {'response': response, 'result': 'error'}
            # c.update(dict);
            return HttpResponse(simplejson.dumps(dict))




def feeds_subcat(request):
    type  = request.GET['type'];
    if type=='1':
        json_subcat = serializers.serialize("json", City.objects.filter(area=request.GET['id']))
    if type=='2':
        json_subcat = serializers.serialize("json", CityArea.objects.filter(cityid=request.GET['id']))
    return HttpResponse(json_subcat, mimetype="application/javascript")


def send_form(request):
    if request.POST:
        value= request.POST['subrealtype']
        #print 'val=='+value
        if value=='1':
            advertform = AdvertForm(request.POST, request.FILES)
            #print 'value1='+str(value)
            id = 'in1'

        if value=='2':
            advertform = AdvertForm2(request.POST, request.FILES)
            #print 'value2='+str(value)
            id = 'in2'

        FormSet = PhotoFormSet(request.POST, request.FILES)
        contactform = ContactInfoForm(request.POST, request.FILES)
        c={'form':advertform,'contactform':contactform,'formset':FormSet}
        c.update(csrf(request))


        values = request.FILES.items()
        #values.sort()
        #html = []
        #for k, v in values:
        #    print '%s =%s' % (k, v)

        if advertform.is_valid()  and contactform.is_valid() and  FormSet.is_valid():
            newadvert = advertform.save(commit=False)
            if request.POST['add_type_cost']=='all':
                cost = float(request.POST['usercost']) / float(request.POST['square'])
                costall = request.POST['usercost']
                cost = str(cost)

            if request.POST['add_type_cost']=='m2':
                costall = float(request.POST['usercost']) * float(request.POST['square'])
                cost = request.POST['usercost']
                costall = str(costall)


            c = request.POST['comissionvalue']
            if c=='':
                c=0
            c = str(c)
            square = request.POST['square']
            ceill_height = request.POST['ceill_height']
            square = str(square)
            ceill_height = str(ceill_height)
            newadvert.square = Decimal(square)
            newadvert.ceill_height = Decimal(ceill_height)
            contactform.comissionvalue = Decimal(c)
            #print 'cost=='+str(cost)
            #print 'costall=='+str(costall)
            newadvert.usercost = Decimal(cost)
            newadvert.usercostforall = Decimal(costall)
            newadvert = advertform.save(commit=False)
            newadvert.planning = newadvert.planning
            newadvert.poster = newadvert.poster
            newadvert.user = request.user

            #contactform.logocompany = unicode(contactform.logocompany)

            newadvert.contact = contactform.save()
            newadvert.save()
            advertform.save_m2m()

            instantces = FormSet.save(commit=False)
            for intance in instantces:
                intance.advert = newadvert
                intance.save()

            return HttpResponse(simplejson.dumps({'result': 'success'}))
            #return HttpResponseRedirect('/advert/thanks/')

        else:
            response = {}
            for k in advertform.errors:
                #print 'error advert==%s'% k
                response[k] = advertform.errors[k][0]

            for k in contactform.errors:
                #print 'error contact==%s'% k
                response[k] = contactform.errors[k][0]

            dict = {'response': response, 'result': 'error'}
            # c.update(dict);

            return HttpResponse(simplejson.dumps(dict))

@dajaxice_register
def add_form(request,value):
    dajax = Dajax()
    import sorl.thumbnail
    import PIL

    if value==1:
        advertform = AdvertForm(
            initial = {'user':request.user},
            #           error_class=DivErrorList,
        )
    if value ==2:
        advertform = AdvertForm2(
            initial = {'user':request.user},
            #          error_class=DivErrorList,
        )

    contactform = ContactInfoForm(
        #         error_class=DivErrorList,
    )
    FormSet = PhotoFormSet(queryset=Photo.objects.none())
    # render = render_to_string('new_house.html')
    c={'form':advertform, 'contactform':contactform,'formset':FormSet}
    c.update(csrf(request))
    if value==1:
        id = 'in1'
        render = render_to_string('advert/add_tab21.html',c )
    if value==2:
        id = 'in2'
        render = render_to_string('advert/add_tab22.html',c)

    dajax.assign('#'+id, 'innerHTML', render)
    return dajax.json()

@dajaxice_register
def edit_add_form(request,adid):
    dajax = Dajax()
    #print "AAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
    adv = Advert.objects.get(pk=adid)
    contact = ContactInfo.objects.get(pk=adv.contact.id)
    pictures = Photo.objects.filter(advert=adid)
    value = adv.realtype.subtype_id
    #countryarea =  CountryArea.objects.get(pk=adv.city.area.id)
    #adv.countryarea =  CountryArea.objects.filter(pk=adv.city.area.id)


    value = int(value)

    if value==1:
        advertform = AdvertFormEdit(instance=adv)
    if value ==2:
        advertform = AdvertForm2Edit(instance=adv)

    contactform = ContactInfoForm(instance=contact)
    FormSet = PhotoFormSet2(queryset=Photo.objects.filter(advert=adid))

    #advertform.id = adid

    # render = render_to_string('new_house.html')
    c={'form':advertform, 'contactform':contactform,'formset':FormSet,'pictures':pictures,'advert_id':adid}
    c.update(csrf(request))
    if value==1:
        id = 'in1'
        render = render_to_string('advert/edit_add_tab21.html',c )
    if value==2:
        id = 'in2'
        render = render_to_string('advert/edit_add_tab22.html',c)

    dajax.assign('#'+id, 'innerHTML', render)
    return dajax.json()




@csrf_protect
@dajaxice_register
def realtypeadd(request, value, fname):
    dajax = Dajax()
    out = ""
    id = 'id_realtype'
    rtype = RealType.objects.filter(subtype=value)
    for o in rtype:
        out +='<option value=%s>%s</option>' % (o.id, o.name)
    dajax.assign('#'+fname+' select#'+id, 'innerHTML', out)
    #    dajax.assign('#'+fname+' select#id_realtype', 'innerHTML', out)
    return dajax.json()

@csrf_protect
@dajaxice_register
def cityarea(request, value, id, namef):
    dajax = Dajax()
    out = ""
    out +='<option value=0>-----</option>'
    if id =='id_city':
        city_list = City.objects.filter(area=value)
        for o in city_list:
            out += '<option value=%s>%s</option>' % (o.id, o.name)

    if id =='id_cityarea':
        area_list = CityArea.objects.filter(cityid=value)
        for o in area_list:
            out += '<option value=%s>%s</option>' % (o.id, o.name)

    #print out
    dajax.assign('#'+namef+' select#'+id, 'innerHTML', out)
    return dajax.json()

@csrf_protect
@dajaxice_register
def updateadd(request, value, id, namef):
    dajax = Dajax()
    c = ""
    c +='<option value=->-----</option>'
    if id=='id_city':
        city_list = City.objects.filter(area=value)
        for o in city_list:
            c +='<option value=%s>%s</option>' % (o.id, o.name)

    if id=='id_cityarea':

        area_list = CityArea.objects.filter(cityid=value)
        for o in area_list:
            c +='<option value=%s>%s</option>' % (o.id, o.name)

    if id=='id_housetype':

        area_list = HouseType.objects.filter(realtype=value)
        for o in area_list:
            c +='<option value=%s>%s</option>' % (o.id, o.name)

    dajax.assign('#'+namef+' select#'+id, 'innerHTML', c)
    return dajax.json()
