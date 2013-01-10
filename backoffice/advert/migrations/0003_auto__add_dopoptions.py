# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'DopOptions'
        db.create_table('advert_dopoptions', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('advert', ['DopOptions'])

        # Adding M2M table for field dopoptions on 'Advert'
        db.create_table('advert_advert_dopoptions', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('advert', models.ForeignKey(orm['advert.advert'], null=False)),
            ('dopoptions', models.ForeignKey(orm['advert.dopoptions'], null=False))
        ))
        db.create_unique('advert_advert_dopoptions', ['advert_id', 'dopoptions_id'])


    def backwards(self, orm):
        
        # Deleting model 'DopOptions'
        db.delete_table('advert_dopoptions')

        # Removing M2M table for field dopoptions on 'Advert'
        db.delete_table('advert_advert_dopoptions')


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
            'advoptions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'\\xd0\\xa3\\xd0\\xb4\\xd0\\xbe\\xd0\\xb1\\xd1\\x81\\xd1\\x82\\xd0\\xb2\\xd0\\xb0'", 'blank': 'True', 'to': "orm['advert.AdvOptions']"}),
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
            'dopoptions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'\\xd0\\x94\\xd0\\xbe\\xd0\\xbf. \\xd0\\xbe\\xd0\\xbf\\xd1\\x86\\xd0\\xb8\\xd0\\xb8'", 'blank': 'True', 'to': "orm['advert.DopOptions']"}),
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
            'operationtype': ('django.db.models.fields.related.ForeignKey', [], {'default': '0', 'to': "orm['advert.OperationType']", 'null': 'True', 'blank': 'True'}),
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
        'advert.dopoptions': {
            'Meta': {'object_name': 'DopOptions'},
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
