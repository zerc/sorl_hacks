# coding: utf-8
from __future__ import unicode_literals

from django.contrib import admin
from django.db.models import TextField

from .utils import create_thumbs


class ThumbedCkeditorImages(admin.ModelAdmin):
    class Meta:
        abstract = True

    def save_model(self, request, obj, form, change):
        for fname in form.changed_data:
            field = obj._meta.get_field_by_name(fname)[0]
            if isinstance(field, TextField):
                setattr(obj, fname, create_thumbs(getattr(obj, fname)))

        super(ThumbedCkeditorImages, self).save_model(
            request, obj, form, change)
