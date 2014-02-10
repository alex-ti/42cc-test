# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Person'
        db.create_table('person_person', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('firstname', self.gf('django.db.models.fields.CharField')(max_length=70)),
            ('lastname', self.gf('django.db.models.fields.CharField')(max_length=70)),
            ('birthday', self.gf('django.db.models.fields.DateField')()),
            ('bio', self.gf('django.db.models.fields.TextField')()),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('jabber', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('skype', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('other', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('person', ['Person'])


    def backwards(self, orm):
        # Deleting model 'Person'
        db.delete_table('person_person')


    models = {
        'person.person': {
            'Meta': {'object_name': 'Person'},
            'bio': ('django.db.models.fields.TextField', [], {}),
            'birthday': ('django.db.models.fields.DateField', [], {}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'firstname': ('django.db.models.fields.CharField', [], {'max_length': '70'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'jabber': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'lastname': ('django.db.models.fields.CharField', [], {'max_length': '70'}),
            'other': ('django.db.models.fields.TextField', [], {}),
            'skype': ('django.db.models.fields.CharField', [], {'max_length': '32'})
        }
    }

    complete_apps = ['person']