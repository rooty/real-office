# -*- coding: utf-8 -*-
from django.forms import ModelForm, CheckboxSelectMultiple
from django.forms.models import modelformset_factory
from advert.models import *
from form_utils.widgets import ImageWidget




#from widgets import CalendarWidget
from django import forms


ROOMSCOUNT = (
    ('','---------'),
    (1,u'1 комната'),
    (2,u'2 комнаты'),
    (3,u'3 комнаты'),
    (4,u'4 комнаты'),
    (5,u'5 комнат'),
    )
PRICEFOR = (
    (1, u'за обьект'),
    (2, u'за m2'),
    )


class SearchForm1(forms.Form):
    operationtype = forms.ModelChoiceField(queryset=OperationType.objects.all(), widget = forms.Select(attrs = {"class":"sel"}))
    countryarea = forms.ModelChoiceField(queryset = CountryArea.objects.all())
    realtype = forms.ModelChoiceField(queryset = RealType.objects.all().filter(subtype__id=2))
    city = forms.ModelChoiceField(queryset = City.objects.all(),widget=forms.Select(attrs={'disabled':'true'}))
    cityarea = forms.ModelChoiceField(queryset = CityArea.objects.all(),widget=forms.Select(attrs={'disabled':'true'}))
    flattype= forms.ModelChoiceField(queryset = FlatType.objects.all())
    housetype= forms.ModelChoiceField(queryset = HouseType.objects.all())
    housematerial= forms.ModelChoiceField(queryset = HouseMaterial.objects.all())
    cost1 = forms.DecimalField(widget = forms.TextInput(attrs = {"class":"t_text"}))
    cost2 = forms.DecimalField(widget = forms.TextInput(attrs = {"class":"t_text"}))
    currency = forms.ModelChoiceField(queryset = Currency.objects.all(), widget = forms.Select(attrs = {"class":"sel"}))
    roomstype = forms.ModelChoiceField(queryset = RoomType.objects.all(), widget = forms.Select(attrs = {"class":"sel"}))
    square1 = forms.FloatField(widget = forms.TextInput(attrs = {"class":"t_text"}))
    square2 = forms.FloatField(widget = forms.TextInput(attrs = {"class":"t_text"}))
    landsize1 = forms.FloatField(widget = forms.TextInput(attrs = {"class":"t_text"}))
    landsize2 = forms.FloatField(widget = forms.TextInput(attrs = {"class":"t_text"}))
    floor1 = forms.IntegerField(widget = forms.TextInput(attrs = {"class":"t_text"}))
    floor2 = forms.IntegerField(widget = forms.TextInput(attrs = {"class":"t_text"}))
    floors1 = forms.CharField(widget = forms.TextInput(attrs = {"class":"t_text"}))
    floors2 = forms.CharField(widget = forms.TextInput(attrs = {"class":"t_text"}))
    usercurrency = forms.ModelChoiceField(queryset=Currency.objects.all(),widget=forms.Select(attrs = {"class":"sel"}))
    roomscount = forms.ChoiceField(choices=ROOMSCOUNT)
    for_object = forms.BooleanField(widget=forms.CheckboxInput(attrs = {"class":"checkbox"}))
    for_m2 = forms.BooleanField(widget=forms.CheckboxInput(attrs = {"class":"checkbox"}))
    pricefor = forms.ChoiceField(choices=PRICEFOR,  widget=forms.RadioSelect,initial=1)
    photoyes = forms.BooleanField(widget=forms.CheckboxInput(attrs = {"class":"checkbox"}))
    videoyes = forms.BooleanField(widget=forms.CheckboxInput(attrs = {"class":"checkbox"}))
    comisionyes = forms.BooleanField(widget=forms.CheckboxInput(attrs = {"class":"checkbox"}))
    stateofrepair = forms.ModelChoiceField(queryset=StateOfRepair.objects.all(),widget=forms.Select(attrs = {"class":"sel"}))
    bussinesperiod = forms.ModelChoiceField(queryset=ArendaBusinessPeriod.objects.all(),widget=forms.Select(attrs = {"class":"sel"}))
    businesscenterclass = forms.ModelChoiceField(queryset=BusinessCenterClass.objects.all(),widget=forms.Select(attrs = {"class":"sel"}))
    separateentrance = forms.ModelChoiceField(queryset=SeparateEntrance.objects.all(),widget=forms.Select(attrs = {"class":"sel"}))
    locationofproperty = forms.ModelChoiceField(queryset=LocationOfProperty.objects.all(),widget=forms.Select(attrs = {"class":"sel"}))
    typeoffund = forms.ModelChoiceField(queryset=TypeOfFund.objects.all(),widget=forms.Select(attrs = {"class":"sel"}))
    metro = forms.ModelChoiceField(queryset=Metro.objects.all(),widget=forms.Select(attrs = {"class":"sel"}))
    ceill_height = forms.FloatField(widget = forms.TextInput(attrs = {"class":"t_text"}))
    wc_count = forms.FloatField(widget = forms.TextInput(attrs = {"class":"t_text"}))
    free_from = forms.DateField(widget = forms.TextInput(attrs = {"class":"s_text"}))
    free_to = forms.DateField(widget = forms.TextInput(attrs = {"class":"s_text"}))
    advoptions  = forms.ModelMultipleChoiceField(queryset=AdvOptions.objects.all(),widget=CheckboxSelectMultiple(attrs = {"class":"checkbox"}))
    dopoptions  = forms.ModelMultipleChoiceField(queryset=DopOptions.objects.all(),widget=CheckboxSelectMultiple(attrs = {"class":"checkbox"}))


class ContactInfoForm(ModelForm):
    fio = forms.CharField(widget=forms.TextInput(attrs = {"class":"input_et required"}))
    tel   = forms.CharField(widget=forms.TextInput(attrs = {"class":"input_et required"}))
    tel2   = forms.CharField(widget=forms.TextInput(attrs = {"class":"input_et"}),required=False)
    email = forms.EmailField(widget=forms.TextInput(attrs = {"class":"input_et required"}))
    skype = forms.CharField(widget=forms.TextInput(attrs = {"class":"input_et"}),required=False)
    #logocompany = forms.ImageField(required=False)
    logocompany = forms.ImageField(widget=ImageWidget(),required=False)
    accounttype = forms.ModelChoiceField(queryset=ContactType.objects.all(),widget=forms.Select(attrs = {"class":"sel required"}))
    comision = forms.ModelChoiceField(queryset=ComisionType.objects.all(),widget=forms.Select(attrs = {"class":"sel required"}))



    class Meta:
        model = ContactInfo



class AdvertForm(ModelForm):
    realtype = forms.ModelChoiceField(queryset=RealType.objects.filter(subtype=1),widget=forms.Select(attrs = {"class":"sel required"}))
    housetype= forms.ModelChoiceField(queryset=HouseType.objects.all(),widget=forms.Select(attrs = {"class":"sel "}),required=False)
    operationtype = forms.ModelChoiceField(queryset=OperationType.objects.all(),widget=forms.Select(attrs = {"class":"sel required"}))
    countryarea = forms.ModelChoiceField(queryset=CountryArea.objects.all(),widget=forms.Select(attrs = {"class":"sel required"}))
    city = forms.ModelChoiceField(queryset=City.objects.all(),widget=forms.Select(attrs = {"class":"sel required",'disabled':'true'}))
    cityarea = forms.ModelChoiceField(queryset=CityArea.objects.all(),widget=forms.Select(attrs = {"class":"sel",'disabled':'true'}),required=False)
    street = forms.ModelChoiceField(queryset=Street.objects.all(),widget=forms.Select(attrs = {"class":"sel required"}),required=False)
    housenumber = forms.CharField(widget=forms.TextInput(attrs = {"class":"input_et"}),required=False)
    housematerial = forms.ModelChoiceField(queryset=HouseMaterial.objects.all(),widget=forms.Select(attrs = {"class":"sel"}),required=False)
    rooms = forms.IntegerField(widget=forms.TextInput(attrs = {"class":"input_et  required"}))
    metro = forms.ModelChoiceField(queryset=Metro.objects.all(),widget=forms.Select(attrs = {"class":"sel"}),required=False)
    planning = forms.ImageField(widget=ImageWidget(),required=False)
    poster = forms.ImageField(widget=ImageWidget(),required=False)
    floor = forms.IntegerField(widget=forms.TextInput(attrs = {"class":"input_et  required"}))
    floors = forms.IntegerField(widget=forms.TextInput(attrs = {"class":"input_et  required"}))
    cost = forms.DecimalField(required=False)
    costforall = forms.DecimalField(required=False)
    usercost = forms.CharField(widget=forms.TextInput(attrs = {"class":"input_et required"}))
    #usercostforall = forms.CharField(widget=forms.TextInput(attrs = {"class":"input_et"}))
    usercurrency = forms.ModelChoiceField(queryset=Currency.objects.all(),empty_label=None,widget=forms.Select(attrs = {"class":"sel"}))
    door = forms.ModelChoiceField(queryset=DoorType.objects.all(),widget=forms.Select(attrs = {"class":"sel "}),required=False)
    accounttype = forms.ModelChoiceField(queryset=ContactType.objects.all(),widget=forms.Select(attrs = {"class":"sel"}))
    desciption = forms.Textarea()
    roomstype = forms.ModelChoiceField(queryset=RoomType.objects.all(),empty_label=None,  widget=forms.RadioSelect(attrs = {"class":"required"}))
    home_deadline = forms.DateField(widget=forms.TextInput(attrs = {"class":"input_et"}),required=False)
    free_from = forms.DateField(widget=forms.TextInput(attrs = {"class":"input_et"}),required=False)
    free_to = forms.DateField(widget=forms.TextInput(attrs = {"class":"input_et"}),required=False)
    wc_count = forms.TextInput(attrs={'class':'input_et'})
    stateofrepair = forms.ModelChoiceField(queryset=StateOfRepair.objects.all(),widget=forms.Select(attrs = {"class":"sel"}),required=False)
    floor_type = forms.ModelChoiceField(queryset=FloorType.objects.all(),widget=forms.Select(attrs = {"class":"sel"}),required=False)
    advoptions  = forms.ModelMultipleChoiceField(queryset=AdvOptions.objects.all(),widget=CheckboxSelectMultiple(attrs = {"class":"checkbox"}),required=False)
    dopoptions  = forms.ModelMultipleChoiceField(queryset=DopOptions.objects.all(),widget=CheckboxSelectMultiple(attrs = {"class":"checkbox"}),required=False)
    flattypeid = metro = forms.ModelChoiceField(queryset=FlatType.objects.all(),widget=forms.Select(attrs = {"class":"sel"}),required=False)
    video = forms.FileField(required=False)
    square = forms.IntegerField(widget=forms.TextInput(attrs = {"class":"input_et  required"}))
    termaccommodation = forms.ModelChoiceField(queryset=TermAccommodation.objects.all(),widget=forms.Select(attrs = {"class":"sel required"}),required=False)


    class Meta:
        model = Advert
        exclude = ('photos','user','contact','cost','costforall','slug','usercostforall')

class AdvertForm2(ModelForm):
    #id = forms.IntegerField(widget=forms.TextInput(attrs = {"class":"input_et"}),required=False)
    realtype = forms.ModelChoiceField(queryset=RealType.objects.filter(subtype=2),widget=forms.Select(attrs = {"class":"sel required"}))
    housetype= forms.ModelChoiceField(queryset=HouseType.objects.all(),widget=forms.Select(attrs = {"class":"sel"}),required=False)
    operationtype = forms.ModelChoiceField(queryset=OperationType.objects.all(),widget=forms.Select(attrs = {"class":"sel required"}))
    countryarea = forms.ModelChoiceField(queryset=CountryArea.objects.all(),widget=forms.Select(attrs = {"class":"sel required"}))
    city = forms.ModelChoiceField(queryset=City.objects.all(),widget=forms.Select(attrs = {"class":"sel required",'disabled':'true'}))
    cityarea = forms.ModelChoiceField(queryset=CityArea.objects.all(),widget=forms.Select(attrs = {"class":"sel",'disabled':'true'}),required=False)
    street = forms.ModelChoiceField(queryset=Street.objects.all(),widget=forms.Select(attrs = {"class":"sel"}),required=False)
    housenumber = forms.CharField(widget=forms.TextInput(attrs = {"class":"input_et"}),required=False)
    cabinetcount = rooms = forms.IntegerField(widget=forms.TextInput(attrs = {"class":"input_et  required"}))
    roomstype = forms.ModelChoiceField(queryset=RoomType.objects.all(),empty_label=None,  widget=forms.RadioSelect(attrs = {"class":"required"}))
    planning = forms.ImageField(widget=ImageWidget(),required=False)
    poster = forms.ImageField(widget=ImageWidget(),required=False)
    metro = forms.ModelChoiceField(queryset=Metro.objects.all(),widget=forms.Select(attrs = {"class":"sel"}),required=False)
    floor = forms.IntegerField(widget=forms.TextInput(attrs = {"class":"input_et  required"}))
    floors = forms.IntegerField(widget=forms.TextInput(attrs = {"class":"input_et  required"}))
    ceill_height = forms.IntegerField(widget=forms.TextInput(attrs = {"class":"input_et  required"}))
    usercost = forms.CharField(widget=forms.TextInput(attrs = {"class":"input_et required"}))
    usercurrency = forms.ModelChoiceField(queryset=Currency.objects.all(),widget=forms.Select(attrs = {"class":"sel required"}))
    accounttype = forms.ModelChoiceField(queryset=ContactType.objects.all(),widget=forms.Select(attrs = {"class":"sel"}))
    typeoffund = forms.ModelChoiceField(queryset=TypeOfFund.objects.all(),widget=forms.Select(attrs = {"class":"sel"}),required=False)
    businesscenterclass = forms.ModelChoiceField(queryset=BusinessCenterClass.objects.all(),widget=forms.Select(attrs = {"class":"sel"}),required=False)
    bussinesperiod = forms.ModelChoiceField(queryset=ArendaBusinessPeriod.objects.all(),widget=forms.Select(attrs = {"class":"sel"}),required=False)
    locationofproperty = forms.ModelChoiceField(queryset=LocationOfProperty.objects.all(),widget=forms.Select(attrs = {"class":"sel"}),required=False)
    separateentrance = forms.ModelChoiceField(queryset=SeparateEntrance.objects.all(),widget=forms.Select(attrs = {"class":"sel"}),required=False)
    home_deadline = forms.DateField(widget=forms.TextInput(attrs = {"class":"input_et"}),required=False)
    free_from = forms.DateField(widget=forms.TextInput(attrs = {"class":"input_et"}),required=False)
    free_to = forms.DateField(widget=forms.TextInput(attrs = {"class":"input_et"}),required=False)
    advoptions  = forms.ModelMultipleChoiceField(queryset=AdvOptions.objects.all(),widget=CheckboxSelectMultiple(attrs = {"class":"checkbox"}),required=False)
    dopoptions  = forms.ModelMultipleChoiceField(queryset=DopOptions.objects.all(),widget=CheckboxSelectMultiple(attrs = {"class":"checkbox"}),required=False)
    video = forms.FileField(required=False)
    square = forms.IntegerField(widget=forms.TextInput(attrs = {"class":"input_et  required"}))
    termaccommodation = forms.ModelChoiceField(queryset=TermAccommodation.objects.all(),widget=forms.Select(attrs = {"class":"sel required"}),required=False)
    rooms = forms.IntegerField(widget=forms.TextInput(attrs = {"class":"input_et"}),required=False)


    class Meta:
        model = Advert
        hidden = ('user','contact')
        exclude = ('photos','user','contact','cost','costforall','slug','rooms','squarelife','flattypeid','usercostforall')



class AdvertFormEdit(ModelForm):
    realtype = forms.ModelChoiceField(queryset=RealType.objects.filter(subtype=1),widget=forms.Select(attrs = {"class":"sel required"}))
    housetype= forms.ModelChoiceField(queryset=HouseType.objects.all(),widget=forms.Select(attrs = {"class":"sel "}),required=False)
    operationtype = forms.ModelChoiceField(queryset=OperationType.objects.all(),widget=forms.Select(attrs = {"class":"sel required"}))
    countryarea = forms.ModelChoiceField(queryset=CountryArea.objects.all(),widget=forms.Select(attrs = {"class":"sel required"}))
    city = forms.ModelChoiceField(queryset=City.objects.all(),widget=forms.Select(attrs = {"class":"sel required",'disabled':'true'}))
    cityarea = forms.ModelChoiceField(queryset=CityArea.objects.all(),widget=forms.Select(attrs = {"class":"sel",'disabled':'true'}),required=False)
    street = forms.ModelChoiceField(queryset=Street.objects.all(),widget=forms.Select(attrs = {"class":"sel required"}),required=False)
    housenumber = forms.CharField(widget=forms.TextInput(attrs = {"class":"input_et"}),required=False)
    housematerial = forms.ModelChoiceField(queryset=HouseMaterial.objects.all(),widget=forms.Select(attrs = {"class":"sel"}),required=False)
    rooms = forms.IntegerField(widget=forms.TextInput(attrs = {"class":"input_et  required"}))
    metro = forms.ModelChoiceField(queryset=Metro.objects.all(),widget=forms.Select(attrs = {"class":"sel"}),required=False)
    planning = forms.ImageField(widget=ImageWidget(),required=False)
    poster = forms.ImageField(widget=ImageWidget(),required=False)
    floor = forms.IntegerField(widget=forms.TextInput(attrs = {"class":"input_et  required"}))
    floors = forms.IntegerField(widget=forms.TextInput(attrs = {"class":"input_et  required"}))
    cost = forms.DecimalField(required=False)
    costforall = forms.DecimalField(required=False)
    usercost = forms.CharField(widget=forms.TextInput(attrs = {"class":"input_et required"}))
    #usercostforall = forms.CharField(widget=forms.TextInput(attrs = {"class":"input_et"}))
    usercurrency = forms.ModelChoiceField(queryset=Currency.objects.all(),empty_label=None,widget=forms.Select(attrs = {"class":"sel"}))
    door = forms.ModelChoiceField(queryset=DoorType.objects.all(),widget=forms.Select(attrs = {"class":"sel "}),required=False)
    accounttype = forms.ModelChoiceField(queryset=ContactType.objects.all(),widget=forms.Select(attrs = {"class":"sel"}))
    desciption = forms.Textarea()
    roomstype = forms.ModelChoiceField(queryset=RoomType.objects.all(),empty_label=None,  widget=forms.RadioSelect(attrs = {"class":"required"}))
    home_deadline = forms.DateField(widget=forms.TextInput(attrs = {"class":"input_et"}),required=False)
    free_from = forms.DateField(widget=forms.TextInput(attrs = {"class":"input_et"}),required=False)
    free_to = forms.DateField(widget=forms.TextInput(attrs = {"class":"input_et"}),required=False)
    wc_count = forms.TextInput(attrs={'class':'input_et'})
    stateofrepair = forms.ModelChoiceField(queryset=StateOfRepair.objects.all(),widget=forms.Select(attrs = {"class":"sel"}),required=False)
    floor_type = forms.ModelChoiceField(queryset=FloorType.objects.all(),widget=forms.Select(attrs = {"class":"sel"}),required=False)
    advoptions  = forms.ModelMultipleChoiceField(queryset=AdvOptions.objects.all(),widget=CheckboxSelectMultiple(attrs = {"class":"checkbox"}),required=False)
    dopoptions  = forms.ModelMultipleChoiceField(queryset=DopOptions.objects.all(),widget=CheckboxSelectMultiple(attrs = {"class":"checkbox"}),required=False)
    flattypeid = metro = forms.ModelChoiceField(queryset=FlatType.objects.all(),widget=forms.Select(attrs = {"class":"sel"}),required=False)
    video = forms.FileField(required=False)
    square = forms.IntegerField(widget=forms.TextInput(attrs = {"class":"input_et  required"}))
    termaccommodation = forms.ModelChoiceField(queryset=TermAccommodation.objects.all(),widget=forms.Select(attrs = {"class":"sel required"}),required=False)


    class Meta:
        model = Advert
        exclude = ('photos','user','contact','cost','costforall','slug')

class AdvertForm2Edit(ModelForm):
    #id = forms.IntegerField(widget=forms.TextInput(attrs = {"class":"input_et"}),required=False)
    realtype = forms.ModelChoiceField(queryset=RealType.objects.filter(subtype=2),widget=forms.Select(attrs = {"class":"sel required"}))
    housetype= forms.ModelChoiceField(queryset=HouseType.objects.all(),widget=forms.Select(attrs = {"class":"sel"}),required=False)
    operationtype = forms.ModelChoiceField(queryset=OperationType.objects.all(),widget=forms.Select(attrs = {"class":"sel required"}))
    countryarea = forms.ModelChoiceField(queryset=CountryArea.objects.all(),widget=forms.Select(attrs = {"class":"sel required"}))
    city = forms.ModelChoiceField(queryset=City.objects.all(),widget=forms.Select(attrs = {"class":"sel required",'disabled':'true'}))
    cityarea = forms.ModelChoiceField(queryset=CityArea.objects.all(),widget=forms.Select(attrs = {"class":"sel",'disabled':'true'}),required=False)
    street = forms.ModelChoiceField(queryset=Street.objects.all(),widget=forms.Select(attrs = {"class":"sel"}),required=False)
    housenumber = forms.CharField(widget=forms.TextInput(attrs = {"class":"input_et"}),required=False)
    cabinetcount = rooms = forms.IntegerField(widget=forms.TextInput(attrs = {"class":"input_et  required"}))
    roomstype = forms.ModelChoiceField(queryset=RoomType.objects.all(),empty_label=None,  widget=forms.RadioSelect(attrs = {"class":"required"}))
    planning = forms.ImageField(widget=ImageWidget(),required=False)
    poster = forms.ImageField(widget=ImageWidget(),required=False)
    metro = forms.ModelChoiceField(queryset=Metro.objects.all(),widget=forms.Select(attrs = {"class":"sel"}),required=False)
    floor = forms.IntegerField(widget=forms.TextInput(attrs = {"class":"input_et  required"}))
    floors = forms.IntegerField(widget=forms.TextInput(attrs = {"class":"input_et  required"}))
    ceill_height = forms.IntegerField(widget=forms.TextInput(attrs = {"class":"input_et  required"}))
    usercost = forms.CharField(widget=forms.TextInput(attrs = {"class":"input_et required"}))
    usercostforall = forms.CharField(widget=forms.TextInput(attrs = {"class":"input_et required"}))
    usercurrency = forms.ModelChoiceField(queryset=Currency.objects.all(),widget=forms.Select(attrs = {"class":"sel required"}))
    accounttype = forms.ModelChoiceField(queryset=ContactType.objects.all(),widget=forms.Select(attrs = {"class":"sel"}))
    typeoffund = forms.ModelChoiceField(queryset=TypeOfFund.objects.all(),widget=forms.Select(attrs = {"class":"sel"}),required=False)
    businesscenterclass = forms.ModelChoiceField(queryset=BusinessCenterClass.objects.all(),widget=forms.Select(attrs = {"class":"sel"}),required=False)
    bussinesperiod = forms.ModelChoiceField(queryset=ArendaBusinessPeriod.objects.all(),widget=forms.Select(attrs = {"class":"sel"}),required=False)
    locationofproperty = forms.ModelChoiceField(queryset=LocationOfProperty.objects.all(),widget=forms.Select(attrs = {"class":"sel"}),required=False)
    separateentrance = forms.ModelChoiceField(queryset=SeparateEntrance.objects.all(),widget=forms.Select(attrs = {"class":"sel"}),required=False)
    home_deadline = forms.DateField(widget=forms.TextInput(attrs = {"class":"input_et"}),required=False)
    free_from = forms.DateField(widget=forms.TextInput(attrs = {"class":"input_et"}),required=False)
    free_to = forms.DateField(widget=forms.TextInput(attrs = {"class":"input_et"}),required=False)
    advoptions  = forms.ModelMultipleChoiceField(queryset=AdvOptions.objects.all(),widget=CheckboxSelectMultiple(attrs = {"class":"checkbox"}),required=False)
    dopoptions  = forms.ModelMultipleChoiceField(queryset=DopOptions.objects.all(),widget=CheckboxSelectMultiple(attrs = {"class":"checkbox"}),required=False)
    video = forms.FileField(required=False)
    square = forms.IntegerField(widget=forms.TextInput(attrs = {"class":"input_et  required"}))
    termaccommodation = forms.ModelChoiceField(queryset=TermAccommodation.objects.all(),widget=forms.Select(attrs = {"class":"sel required"}),required=False)
    rooms = forms.IntegerField(widget=forms.TextInput(attrs = {"class":"input_et"}),required=False)


    class Meta:
        model = Advert
        hidden = ('user','contact')
        exclude = ('photos','user','contact','cost','costforall','slug','rooms','squarelife','flattypeid')



class PhotoForm(forms.ModelForm):
    picture = forms.ImageField(
        widget=ImageWidget(template='%(input)s<br />%(image)s'),required=False)
    class Meta:
        model = Photo


PhotoFormSet = modelformset_factory(Photo, form=PhotoForm, extra=1, max_num=15, can_delete=True)

PhotoFormSet2 = modelformset_factory(Photo, form=PhotoForm, extra=0, max_num=15, can_delete=True)