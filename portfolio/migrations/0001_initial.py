# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Categories'
        db.create_table(u'portfolio_categories', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('content', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50)),
        ))
        db.send_create_signal(u'portfolio', ['Categories'])

        # Adding model 'Images'
        db.create_table(u'portfolio_images', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['portfolio.Categories'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('caption', self.gf('django.db.models.fields.CharField')(max_length=250, null=True, blank=True)),
            ('year', self.gf('django.db.models.fields.CharField')(max_length=4, null=True, blank=True)),
            ('photo', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
        ))
        db.send_create_signal(u'portfolio', ['Images'])

        # Adding model 'Videos'
        db.create_table(u'portfolio_videos', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['portfolio.Categories'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('caption', self.gf('django.db.models.fields.CharField')(max_length=250, null=True, blank=True)),
            ('year', self.gf('django.db.models.fields.CharField')(max_length=4, null=True, blank=True)),
            ('provider', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('url', self.gf('django.db.models.fields.CharField')(max_length=250)),
        ))
        db.send_create_signal(u'portfolio', ['Videos'])


    def backwards(self, orm):
        # Deleting model 'Categories'
        db.delete_table(u'portfolio_categories')

        # Deleting model 'Images'
        db.delete_table(u'portfolio_images')

        # Deleting model 'Videos'
        db.delete_table(u'portfolio_videos')


    models = {
        u'portfolio.categories': {
            'Meta': {'object_name': 'Categories'},
            'content': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        },
        u'portfolio.images': {
            'Meta': {'object_name': 'Images'},
            'caption': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['portfolio.Categories']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'year': ('django.db.models.fields.CharField', [], {'max_length': '4', 'null': 'True', 'blank': 'True'})
        },
        u'portfolio.videos': {
            'Meta': {'object_name': 'Videos'},
            'caption': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['portfolio.Categories']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'provider': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'year': ('django.db.models.fields.CharField', [], {'max_length': '4', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['portfolio']