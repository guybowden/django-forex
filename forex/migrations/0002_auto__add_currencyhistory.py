# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'CurrencyHistory'
        db.create_table(u'forex_currencyhistory', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('currency', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['forex.Currency'])),
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('rate', self.gf('django.db.models.fields.FloatField')(default=1.0)),
        ))
        db.send_create_signal(u'forex', ['CurrencyHistory'])


    def backwards(self, orm):
        # Deleting model 'CurrencyHistory'
        db.delete_table(u'forex_currencyhistory')


    models = {
        u'forex.currency': {
            'Meta': {'object_name': 'Currency'},
            'base': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'code': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '3'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'rate': ('django.db.models.fields.FloatField', [], {'default': '1.0'}),
            'symbol': ('django.db.models.fields.CharField', [], {'max_length': '3', 'null': 'True', 'blank': 'True'})
        },
        u'forex.currencyhistory': {
            'Meta': {'object_name': 'CurrencyHistory'},
            'currency': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['forex.Currency']"}),
            'date': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'rate': ('django.db.models.fields.FloatField', [], {'default': '1.0'})
        }
    }

    complete_apps = ['forex']