# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Currency'
        db.create_table(u'forex_currency', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('symbol', self.gf('django.db.models.fields.CharField')(max_length=3, null=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('code', self.gf('django.db.models.fields.CharField')(unique=True, max_length=3)),
            ('rate', self.gf('django.db.models.fields.FloatField')(default=1.0)),
            ('base', self.gf('django.db.models.fields.CharField')(max_length=3)),
        ))
        db.send_create_signal(u'forex', ['Currency'])


    def backwards(self, orm):
        # Deleting model 'Currency'
        db.delete_table(u'forex_currency')


    models = {
        u'forex.currency': {
            'Meta': {'object_name': 'Currency'},
            'base': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'code': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '3'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'rate': ('django.db.models.fields.FloatField', [], {'default': '1.0'}),
            'symbol': ('django.db.models.fields.CharField', [], {'max_length': '3', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['forex']