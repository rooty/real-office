# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'OfficeContactInfo'
        db.create_table('office_officecontactinfo', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('owner', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
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
        db.send_create_signal('office', ['OfficeContactInfo'])


    def backwards(self, orm):
        
        # Deleting model 'OfficeContactInfo'
        db.delete_table('office_officecontactinfo')


    models = {
        'advert.comisiontype': {
            'Meta': {'object_name': 'ComisionType'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        'advert.contacttype': {
            'Meta': {'object_name': 'ContactType'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'})
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
        },
        'office.message': {
            'Meta': {'ordering': "['-created']", 'object_name': 'Message'},
            'body': ('django.db.models.fields.TextField', [], {}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'delivery': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'readed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'subject': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_from': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'user_from_message'", 'to': "orm['auth.User']"}),
            'user_to': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'user_to_message'", 'to': "orm['auth.User']"})
        },
        'office.messagefolder': {
            'Meta': {'ordering': "['name']", 'object_name': 'MessageFolder'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        'office.officecontactinfo': {
            'Meta': {'object_name': 'OfficeContactInfo'},
            'accounttype': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['advert.ContactType']"}),
            'comision': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['advert.ComisionType']"}),
            'comissionvalue': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '20', 'decimal_places': '2', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '128'}),
            'fio': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'logocompany': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'skype': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'}),
            'tel': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'tel2': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'})
        },
        'office.project': {
            'Meta': {'ordering': "['-date_start']", 'object_name': 'Project'},
            'date_end': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2012, 2, 20, 3, 49, 41, 660734)'}),
            'date_start': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2012, 2, 20, 3, 49, 41, 660691)'}),
            'description': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'percenttask': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        'office.task': {
            'Meta': {'ordering': "['-created']", 'object_name': 'Task'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_end': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2012, 2, 20, 3, 49, 41, 662040)'}),
            'description': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'priority': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['office.Project']"}),
            'state': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['office.TaskState']"}),
            'terminate': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'worker': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'null': 'True'})
        },
        'office.taskstate': {
            'Meta': {'object_name': 'TaskState'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        }
    }

    complete_apps = ['office']
