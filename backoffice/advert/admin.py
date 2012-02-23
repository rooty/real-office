# -*- coding: utf-8 -*-
from django.contrib import admin
from models import *

class AdvertAdmin(admin.ModelAdmin):
    list_display = (
	'get_slug_name',
	'city',
	'street',
    )
    
admin.site.register(Metro)
admin.site.register(ContactInfo)
admin.site.register(DopOptions)
admin.site.register(ContactType)
admin.site.register(Currency)
admin.site.register(OperationType)
admin.site.register(CountryArea)
admin.site.register(RealType)
admin.site.register(RealType2)
admin.site.register(City)
admin.site.register(CityArea)
admin.site.register(Street)
admin.site.register(FlatType)
admin.site.register(HouseMaterial)
admin.site.register(HouseType)
admin.site.register(AdvOptions)
admin.site.register(AdvContact)
admin.site.register(TrassaDirection)
admin.site.register(LandPurpose)
admin.site.register(Photo)
admin.site.register(UserCart)
admin.site.register(DoorType)
admin.site.register(ComisionType)
admin.site.register(RoomType)
admin.site.register(FloorType)
admin.site.register(StateOfRepair)
admin.site.register(TermAccommodation)
admin.site.register(TypeOfFund)
admin.site.register(LocationOfProperty)
admin.site.register(BusinessCenterClass)
admin.site.register(SeparateEntrance)
admin.site.register(ArendaBusinessPeriod)
admin.site.register(Advert, AdvertAdmin)
