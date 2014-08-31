# coding: utf-8
from __future__ import unicode_literals

from django.db import models
from django.conf import settings
from django.utils.safestring import mark_safe

from sorl.thumbnail import get_thumbnail


__ALL__ = ('ThumbMixin',)


THUMBNAIL_OPTIONS = getattr(
    settings,
    'THUMBNAIL_OPTIONS',
    dict(crop='center', upscaled=False, quality=100))

THUMBNAIL_EMPTY = getattr(settings, 'THUMBNAIL_EMPTY', None)


class ThumbMixin(object):
    """
    Add property to model for generated thumb.
    Usefull in Django templates:

    ::

        {{ my_model.get_thumb_56x56.html }}

    Insted of:

    ::
        {% thumbnail my_model.pic "56x56" crop="center" as im %}
            <img src="{{ im.url }}" width="56" height="56">
        {% empty %}
            <img src="{{ MISSING_IMAGE }}" width="56" height="56">
        {% endthumbnail %}
    """
    @property
    def image_file_field(self):
        try:
            return self.image
        except AttributeError:
            raise NotImplementedError('Set up image_file_field property')

    def __getattr__(self, name):
        prefix = 'get_thumb_'
        if name.startswith(prefix):
            size = name.replace(prefix, '')
            return self._get_thumb(size)
        raise AttributeError(name)

    def _get_thumb(self, size):
        if not self.image_file_field:
            return THUMBNAIL_EMPTY

        tmpl = '<img src="{0.url}" width="{0.width}" height="{0.height}">'
        thumb = get_thumbnail(
            self.image_file_field.file, size, **THUMBNAIL_OPTIONS)
        thumb.html = mark_safe(tmpl.format(thumb))
        return thumb
