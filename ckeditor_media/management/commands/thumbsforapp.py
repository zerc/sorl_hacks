# coding: utf-8
from __future__ import unicode_literals

from django.core.management.base import AppCommand, CommandError
from django.db.models import get_models
from ckeditor.fields import RichTextField

from ckeditor_media.utils import create_thumbs


class Command(AppCommand):
    help = 'Generate thumbs for models of app'

    def handle_app(self, app, **kwargs):
        for model in get_models(app):
            affected_fields = [f.name for f in model._meta.fields
                               if isinstance(f, RichTextField)]

            if not affected_fields:
                continue

            self.proccess(model, affected_fields)

    def proccess(self, model, fields):
        i = 0
        for i, obj in enumerate(model.objects.all()):
            for fname in fields:
                setattr(obj, fname, create_thumbs(getattr(obj, fname)))
            obj.save()

        print('>> {} {} updated'.format(i, repr(model)))
