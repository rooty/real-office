# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'ComisionType'
        db.create_table('advert_comisiontype', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=128)),
        ))
        db.send_create_signal('advert', ['ComisionType'])

        # Adding model 'ContactType'
        db.create_table('advert_contacttype', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=128)),
        ))
        db.send_create_signal('advert', ['ContactType'])

        # Adding model 'ContactInfo'
        db.create_table('advert_contactinfo', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('fio', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('tel', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('tel2', self.gf('django.db.models.fields.CharField')(max_length=128, blank=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=128)),
            ('skype', self.gf('django.db.models.fields.CharField')(max_length=128, blank=True)),
            ('logocompany', self.gf('django.db.models.fields.files.ImageField')(max_length=100, blank=True)),
            ('accounttype', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['advert.ContactType'])),
            ('comision', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['advert.ComisionType'])),
            ('comissionvalue', self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=20, decimal_places=2, blank=True)),
        ))
        db.send_create_signal('advert', ['ContactInfo'])

        # Adding model 'OperationType'
        db.create_table('advert_operationtype', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('advert', ['OperationType'])

        # Adding model 'DoorType'
        db.create_table('advert_doortype', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('advert', ['DoorType'])

        # Adding model 'RealType2'
        db.create_table('advert_realtype2', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('advert', ['RealType2'])

        # Adding model 'RealType'
        db.create_table('advert_realtype', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('subtype', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['advert.RealType2'])),
        ))
        db.send_create_signal('advert', ['RealType'])

        # Adding model 'CountryArea'
        db.create_table('advert_countryarea', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('advert', ['CountryArea'])

        # Adding model 'City'
        db.create_table('advert_city', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('area', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['advert.CountryArea'])),
        ))
        db.send_create_signal('advert', ['City'])

        # Adding model 'CityArea'
        db.create_table('advert_cityarea', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('cityid', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['advert.City'])),
        ))
        db.send_create_signal('advert', ['CityArea'])

        # Adding model 'Metro'
        db.create_table('advert_metro', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('city', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['advert.City'])),
        ))
        db.send_create_signal('advert', ['Metro'])

        # Adding model 'Street'
        db.create_table('advert_street', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('cityid', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['advert.City'])),
        ))
        db.send_create_signal('advert', ['Street'])

        # Adding model 'FlatType'
        db.create_table('advert_flattype', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('advert', ['FlatType'])

        # Adding model 'HouseMaterial'
        db.create_table('advert_housematerial', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('advert', ['HouseMaterial'])

        # Adding model 'HouseType'
        db.create_table('advert_housetype', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('realtype', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['advert.RealType'])),
        ))
        db.send_create_signal('advert', ['HouseType'])

        # Adding model 'AdvOptions'
        db.create_table('advert_advoptions', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('advert', ['AdvOptions'])

        # Adding model 'AdvContact'
        db.create_table('advert_advcontact', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('contact', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=32)),
        ))
        db.send_create_signal('advert', ['AdvContact'])

        # Adding model 'TrassaDirection'
        db.create_table('advert_trassadirection', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('advert', ['TrassaDirection'])

        # Adding model 'LandPurpose'
        db.create_table('advert_landpurpose', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('advert', ['LandPurpose'])

        # Adding model 'Photo'
        db.create_table('advert_photo', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('picture', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('created', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal('advert', ['Photo'])

        # Adding model 'RoomType'
        db.create_table('advert_roomtype', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=128)),
        ))
        db.send_create_signal('advert', ['RoomType'])

        # Adding model 'Currency'
        db.create_table('advert_currency', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=128)),
        ))
        db.send_create_signal('advert', ['Currency'])

        # Adding model 'FloorType'
        db.create_table('advert_floortype', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=128)),
        ))
        db.send_create_signal('advert', ['FloorType'])

        # Adding model 'StateOfRepair'
        db.create_table('advert_stateofrepair', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=128)),
        ))
        db.send_create_signal('advert', ['StateOfRepair'])

        # Adding model 'TermAccommodation'
        db.create_table('advert_termaccommodation', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=128)),
        ))
        db.send_create_signal('advert', ['TermAccommodation'])

        # Adding model 'TypeOfFund'
        db.create_table('advert_typeoffund', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=128)),
        ))
        db.send_create_signal('advert', ['TypeOfFund'])

        # Adding model 'LocationOfProperty'
        db.create_table('advert_locationofproperty', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=128)),
        ))
        db.send_create_signal('advert', ['LocationOfProperty'])

        # Adding model 'BusinessCenterClass'
        db.create_table('advert_businesscenterclass', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=128)),
        ))
        db.send_create_signal('advert', ['BusinessCenterClass'])

        # Adding model 'SeparateEntrance'
        db.create_table('advert_separateentrance', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=128)),
        ))
        db.send_create_signal('advert', ['SeparateEntrance'])

        # Adding model 'ArendaBusinessPeriod'
        db.create_table('advert_arendabusinessperiod', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=128)),
        ))
        db.send_create_signal('advert', ['ArendaBusinessPeriod'])

        # Adding model 'Advert'
        db.create_table('advert_advert', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('realtype', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['advert.RealType'])),
            ('city', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['advert.City'])),
            ('cityarea', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['advert.CityArea'], null=True, blank=True)),
            ('street', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['advert.Street'], null=True, blank=True)),
            ('housenumber', self.gf('django.db.models.fields.CharField')(max_length=32, blank=True)),
            ('housematerial', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['advert.HouseMaterial'], null=True, blank=True)),
            ('housetype', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['advert.HouseType'])),
            ('rooms', self.gf('django.db.models.fields.IntegerField')(default=0, blank=True)),
            ('roomstype', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['advert.RoomType'])),
            ('floor', self.gf('django.db.models.fields.IntegerField')()),
            ('floors', self.gf('django.db.models.fields.IntegerField')()),
            ('trassadirection', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['advert.TrassaDirection'], null=True, blank=True)),
            ('landpurpose', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['advert.LandPurpose'], null=True, blank=True)),
            ('landsize', self.gf('django.db.models.fields.CharField')(default='', max_length=10, null=True, blank=True)),
            ('title', self.gf('django.db.models.fields.CharField')(default='', max_length=255, blank=True)),
            ('desciption', self.gf('django.db.models.fields.TextField')(default='', blank=True)),
            ('square', self.gf('django.db.models.fields.FloatField')(default=0)),
            ('squarelife', self.gf('django.db.models.fields.FloatField')(default=0, blank=True)),
            ('kitchen', self.gf('django.db.models.fields.FloatField')(default=0, null=True, blank=True)),
            ('home_deadline', self.gf('django.db.models.fields.CharField')(max_length=128, null=True, blank=True)),
            ('free_from', self.gf('django.db.models.fields.CharField')(max_length=128, null=True, blank=True)),
            ('free_to', self.gf('django.db.models.fields.CharField')(max_length=128, null=True, blank=True)),
            ('floor_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['advert.FloorType'], null=True, blank=True)),
            ('wc_count', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('stateofrepair', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['advert.StateOfRepair'], null=True, blank=True)),
            ('ceill_height', self.gf('django.db.models.fields.DecimalField')(default=0, null=True, max_digits=20, decimal_places=2, blank=True)),
            ('distance', self.gf('django.db.models.fields.CharField')(default='', max_length=128, null=True, blank=True)),
            ('hotadv', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('cost', self.gf('django.db.models.fields.DecimalField')(max_digits=20, decimal_places=2, blank=True)),
            ('costforall', self.gf('django.db.models.fields.DecimalField')(max_digits=20, decimal_places=2, blank=True)),
            ('usercost', self.gf('django.db.models.fields.DecimalField')(max_digits=20, decimal_places=2)),
            ('usercostforall', self.gf('django.db.models.fields.DecimalField')(max_digits=20, decimal_places=2)),
            ('usercurrency', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['advert.Currency'])),
            ('publication_date', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
            ('viewcount', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('metro', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['advert.Metro'], null=True, blank=True)),
            ('door', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['advert.DoorType'], null=True, blank=True)),
            ('term_accommodation', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['advert.TermAccommodation'], null=True, blank=True)),
            ('typeoffund', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['advert.TypeOfFund'], null=True, blank=True)),
            ('locationofproperty', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['advert.LocationOfProperty'], null=True, blank=True)),
            ('businesscenterclass', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['advert.BusinessCenterClass'], null=True, blank=True)),
            ('separateentrance', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['advert.SeparateEntrance'], null=True, blank=True)),
            ('cabinetcount', self.gf('django.db.models.fields.CharField')(max_length=256, blank=True)),
            ('bussinesperiod', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['advert.ArendaBusinessPeriod'], null=True, blank=True)),
            ('planning', self.gf('django.db.models.fields.files.ImageField')(max_length=256, blank=True)),
            ('poster', self.gf('django.db.models.fields.files.ImageField')(max_length=256, blank=True)),
            ('contact', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['advert.ContactInfo'])),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('torg', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('slug', self.gf('autoslug.fields.AutoSlugField')(unique=True, max_length=50, populate_from=None, unique_with=(), db_index=True)),
        ))
        db.send_create_signal('advert', ['Advert'])

        # Adding M2M table for field advoptions on 'Advert'
        db.create_table('advert_advert_advoptions', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('advert', models.ForeignKey(orm['advert.advert'], null=False)),
            ('advoptions', models.ForeignKey(orm['advert.advoptions'], null=False))
        ))
        db.create_unique('advert_advert_advoptions', ['advert_id', 'advoptions_id'])

        # Adding M2M table for field photos on 'Advert'
        db.create_table('advert_advert_photos', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('advert', models.ForeignKey(orm['advert.advert'], null=False)),
            ('photo', models.ForeignKey(orm['advert.photo'], null=False))
        ))
        db.create_unique('advert_advert_photos', ['advert_id', 'photo_id'])

        # Adding model 'PhotoAdvert'
        db.create_table('advert_photoadvert', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('photo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['advert.Photo'])),
            ('advert', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['advert.Advert'])),
        ))
        db.send_create_signal('advert', ['PhotoAdvert'])

        # Adding model 'ContactAdvert'
        db.create_table('advert_contactadvert', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('photo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['advert.ContactInfo'])),
            ('advert', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['advert.Advert'])),
        ))
        db.send_create_signal('advert', ['ContactAdvert'])

        # Adding model 'UserCart'
        db.create_table('advert_usercart', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('cart_date', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('advert', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['advert.Advert'])),
        ))
        db.send_create_signal('advert', ['UserCart'])


    def backwards(self, orm):
        
        # Deleting model 'ComisionType'
        db.delete_table('advert_comisiontype')

        # Deleting model 'ContactType'
        db.delete_table('advert_contacttype')

        # Deleting model 'ContactInfo'
        db.delete_table('advert_contactinfo')

        # Deleting model 'OperationType'
        db.delete_table('advert_operationtype')

        # Deleting model 'DoorType'
        db.delete_table('advert_doortype')

        # Deleting model 'RealType2'
        db.delete_table('advert_realtype2')

        # Deleting model 'RealType'
        db.delete_table('advert_realtype')

        # Deleting model 'CountryArea'
        db.delete_table('advert_countryarea')

        # Deleting model 'City'
        db.delete_table('advert_city')

        # Deleting model 'CityArea'
        db.delete_table('advert_cityarea')

        # Deleting model 'Metro'
        db.delete_table('advert_metro')

        # Deleting model 'Street'
        db.delete_table('advert_street')

        # Deleting model 'FlatType'
        db.delete_table('advert_flattype')

        # Deleting model 'HouseMaterial'
        db.delete_table('advert_housematerial')

        # Deleting model 'HouseType'
        db.delete_table('advert_housetype')

        # Deleting model 'AdvOptions'
        db.delete_table('advert_advoptions')

        # Deleting model 'AdvContact'
        db.delete_table('advert_advcontact')

        # Deleting model 'TrassaDirection'
        db.delete_table('advert_trassadirection')

        # Deleting model 'LandPurpose'
        db.delete_table('advert_landpurpose')

        # Deleting model 'Photo'
        db.delete_table('advert_photo')

        # Deleting model 'RoomType'
        db.delete_table('advert_roomtype')

        # Deleting model 'Currency'
        db.delete_table('advert_currency')

        # Deleting model 'FloorType'
        db.delete_table('advert_floortype')

        # Deleting model 'StateOfRepair'
        db.delete_table('advert_stateofrepair')

        # Deleting model 'TermAccommodation'
        db.delete_table('advert_termaccommodation')

        # Deleting model 'TypeOfFund'
        db.delete_table('advert_typeoffund')

        # Deleting model 'LocationOfProperty'
        db.delete_table('advert_locationofproperty')

        # Deleting model 'BusinessCenterClass'
        db.delete_table('advert_businesscenterclass')

        # Deleting model 'SeparateEntrance'
        db.delete_table('advert_separateentrance')

        # Deleting model 'ArendaBusinessPeriod'
        db.delete_table('advert_arendabusinessperiod')

        # Deleting model 'Advert'
        db.delete_table('advert_advert')

        # Removing M2M table for field advoptions on 'Advert'
        db.delete_table('advert_advert_advoptions')

        # Removing M2M table for field photos on 'Advert'
        db.delete_table('advert_advert_photos')

        # Deleting model 'PhotoAdvert'
        db.delete_table('advert_photoadvert')

        # Deleting model 'ContactAdvert'
        db.delete_table('advert_contactadvert')

        # Deleting model 'UserCart'
        db.delete_table('advert_usercart')


    models = {
        'advert.advcontact': {
            'Meta': {'object_name': 'AdvContact'},
            'contact': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '32'})
        },
        'advert.advert': {
            'Meta': {'ordering': "['-publication_date']", 'object_name': 'Advert'},
            'advoptions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'\\xd0\\x94\\xd0\\xbe\\xd0\\xbf\\xd0\\xbe\\xd0\\xbb\\xd0\\xbd\\xd0\\xb8\\xd1\\x82\\xd0\\xb5\\xd0\\xbb\\xd1\\x8c\\xd0\\xbd\\xd1\\x8b\\xd0\\xb5 \\xd0\\xbe\\xd0\\xbf\\xd1\\x86\\xd0\\xb8\\xd0\\xb8'", 'blank': 'True', 'to': "orm['advert.AdvOptions']"}),
            'businesscenterclass': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['advert.BusinessCenterClass']", 'null': 'True', 'blank': 'True'}),
            'bussinesperiod': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['advert.ArendaBusinessPeriod']", 'null': 'True', 'blank': 'True'}),
            'cabinetcount': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            'ceill_height': ('django.db.models.fields.DecimalField', [], {'default': '0', 'null': 'True', 'max_digits': '20', 'decimal_places': '2', 'blank': 'True'}),
            'city': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['advert.City']"}),
            'cityarea': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['advert.CityArea']", 'null': 'True', 'blank': 'True'}),
            'contact': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['advert.ContactInfo']"}),
            'cost': ('django.db.models.fields.DecimalField', [], {'max_digits': '20', 'decimal_places': '2', 'blank': 'True'}),
            'costforall': ('django.db.models.fields.DecimalField', [], {'max_digits': '20', 'decimal_places': '2', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'desciption': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'distance': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'door': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['advert.DoorType']", 'null': 'True', 'blank': 'True'}),
            'floor': ('django.db.models.fields.IntegerField', [], {}),
            'floor_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['advert.FloorType']", 'null': 'True', 'blank': 'True'}),
            'floors': ('django.db.models.fields.IntegerField', [], {}),
            'free_from': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'free_to': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'home_deadline': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'hotadv': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'housematerial': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['advert.HouseMaterial']", 'null': 'True', 'blank': 'True'}),
            'housenumber': ('django.db.models.fields.CharField', [], {'max_length': '32', 'blank': 'True'}),
            'housetype': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['advert.HouseType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'kitchen': ('django.db.models.fields.FloatField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'landpurpose': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['advert.LandPurpose']", 'null': 'True', 'blank': 'True'}),
            'landsize': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'locationofproperty': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['advert.LocationOfProperty']", 'null': 'True', 'blank': 'True'}),
            'metro': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['advert.Metro']", 'null': 'True', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'photos': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'\\xd0\\xa4\\xd0\\xbe\\xd1\\x82\\xd0\\xbe\\xd0\\xb3\\xd1\\x80\\xd0\\xb0\\xd1\\x84\\xd0\\xb8\\xd0\\xb8 \\xd0\\xbe\\xd0\\xb1\\xd1\\x8a\\xd0\\xb5\\xd0\\xba\\xd1\\x82\\xd0\\xb0'", 'blank': 'True', 'to': "orm['advert.Photo']"}),
            'planning': ('django.db.models.fields.files.ImageField', [], {'max_length': '256', 'blank': 'True'}),
            'poster': ('django.db.models.fields.files.ImageField', [], {'max_length': '256', 'blank': 'True'}),
            'publication_date': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'realtype': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['advert.RealType']"}),
            'rooms': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'roomstype': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['advert.RoomType']"}),
            'separateentrance': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['advert.SeparateEntrance']", 'null': 'True', 'blank': 'True'}),
            'slug': ('autoslug.fields.AutoSlugField', [], {'unique': 'True', 'max_length': '50', 'populate_from': 'None', 'unique_with': '()', 'db_index': 'True'}),
            'square': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'squarelife': ('django.db.models.fields.FloatField', [], {'default': '0', 'blank': 'True'}),
            'stateofrepair': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['advert.StateOfRepair']", 'null': 'True', 'blank': 'True'}),
            'street': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['advert.Street']", 'null': 'True', 'blank': 'True'}),
            'term_accommodation': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['advert.TermAccommodation']", 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255', 'blank': 'True'}),
            'torg': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'trassadirection': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['advert.TrassaDirection']", 'null': 'True', 'blank': 'True'}),
            'typeoffund': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['advert.TypeOfFund']", 'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'usercost': ('django.db.models.fields.DecimalField', [], {'max_digits': '20', 'decimal_places': '2'}),
            'usercostforall': ('django.db.models.fields.DecimalField', [], {'max_digits': '20', 'decimal_places': '2'}),
            'usercurrency': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['advert.Currency']"}),
            'viewcount': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'wc_count': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'advert.advoptions': {
            'Meta': {'object_name': 'AdvOptions'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'advert.arendabusinessperiod': {
            'Meta': {'object_name': 'ArendaBusinessPeriod'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        'advert.businesscenterclass': {
            'Meta': {'object_name': 'BusinessCenterClass'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        'advert.city': {
            'Meta': {'object_name': 'City'},
            'area': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['advert.CountryArea']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'advert.cityarea': {
            'Meta': {'object_name': 'CityArea'},
            'cityid': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['advert.City']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'advert.comisiontype': {
            'Meta': {'object_name': 'ComisionType'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        'advert.contactadvert': {
            'Meta': {'object_name': 'ContactAdvert'},
            'advert': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['advert.Advert']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'photo': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['advert.ContactInfo']"})
        },
        'advert.contactinfo': {
            'Meta': {'object_name': 'ContactInfo'},
            'accounttype': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['advert.ContactType']"}),
            'comision': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['advert.ComisionType']"}),
            'comissionvalue': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '20', 'decimal_places': '2', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '128'}),
            'fio': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'logocompany': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'skype': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'}),
            'tel': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'tel2': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'})
        },
        'advert.contacttype': {
            'Meta': {'object_name': 'ContactType'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        'advert.countryarea': {
            'Meta': {'object_name': 'CountryArea'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'advert.currency': {
            'Meta': {'object_name': 'Currency'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        'advert.doortype': {
            'Meta': {'object_name': 'DoorType'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'advert.flattype': {
            'Meta': {'object_name': 'FlatType'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'advert.floortype': {
            'Meta': {'object_name': 'FloorType'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        'advert.housematerial': {
            'Meta': {'object_name': 'HouseMaterial'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'advert.housetype': {
            'Meta': {'object_name': 'HouseType'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'realtype': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['advert.RealType']"})
        },
        'advert.landpurpose': {
            'Meta': {'object_name': 'LandPurpose'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'advert.locationofproperty': {
            'Meta': {'object_name': 'LocationOfProperty'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        'advert.metro': {
            'Meta': {'object_name': 'Metro'},
            'city': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['advert.City']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'advert.operationtype': {
            'Meta': {'object_name': 'OperationType'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'advert.photo': {
            'Meta': {'ordering': "('-created',)", 'object_name': 'Photo'},
            'created': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'picture': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'advert.photoadvert': {
            'Meta': {'object_name': 'PhotoAdvert'},
            'advert': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['advert.Advert']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'photo': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['advert.Photo']"})
        },
        'advert.realtype': {
            'Meta': {'object_name': 'RealType'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'subtype': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['advert.RealType2']"})
        },
        'advert.realtype2': {
            'Meta': {'object_name': 'RealType2'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'advert.roomtype': {
            'Meta': {'object_name': 'RoomType'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        'advert.separateentrance': {
            'Meta': {'object_name': 'SeparateEntrance'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        'advert.stateofrepair': {
            'Meta': {'object_name': 'StateOfRepair'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        'advert.street': {
            'Meta': {'object_name': 'Street'},
            'cityid': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['advert.City']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'advert.termaccommodation': {
            'Meta': {'object_name': 'TermAccommodation'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        'advert.trassadirection': {
            'Meta': {'object_name': 'TrassaDirection'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'advert.typeoffund': {
            'Meta': {'object_name': 'TypeOfFund'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        'advert.usercart': {
            'Meta': {'ordering': "['cart_date']", 'object_name': 'UserCart'},
            'advert': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['advert.Advert']"}),
            'cart_date': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['advert']
