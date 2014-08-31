# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'TextBlock.body'
        db.alter_column(u'blog_textblock', 'body', self.gf('ckeditor.fields.RichTextField')())
        # Adding field 'BlogPost.image'
        db.add_column(u'blog_blogpost', 'image',
                      self.gf('sorl.thumbnail.fields.ImageField')(max_length=100, null=True, blank=True),
                      keep_default=False)


        # Changing field 'BlogPost.body'
        db.alter_column(u'blog_blogpost', 'body', self.gf('ckeditor.fields.RichTextField')())

        # Changing field 'BlogPost.lead'
        db.alter_column(u'blog_blogpost', 'lead', self.gf('ckeditor.fields.RichTextField')())

    def backwards(self, orm):

        # Changing field 'TextBlock.body'
        db.alter_column(u'blog_textblock', 'body', self.gf('django.db.models.fields.TextField')())
        # Deleting field 'BlogPost.image'
        db.delete_column(u'blog_blogpost', 'image')


        # Changing field 'BlogPost.body'
        db.alter_column(u'blog_blogpost', 'body', self.gf('django.db.models.fields.TextField')())

        # Changing field 'BlogPost.lead'
        db.alter_column(u'blog_blogpost', 'lead', self.gf('django.db.models.fields.TextField')())

    models = {
        u'blog.blogpost': {
            'Meta': {'object_name': 'BlogPost'},
            'body': ('ckeditor.fields.RichTextField', [], {}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'blog_posts'", 'null': 'True', 'to': u"orm['blog.Category']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'lead': ('ckeditor.fields.RichTextField', [], {}),
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "u'blog_post'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['blog.Tag']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'blog.category': {
            'Meta': {'object_name': 'Category'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'blog.tag': {
            'Meta': {'object_name': 'Tag'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'blog.textblock': {
            'Meta': {'object_name': 'TextBlock'},
            'blog_post': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'blocks'", 'to': u"orm['blog.BlogPost']"}),
            'body': ('ckeditor.fields.RichTextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['blog']