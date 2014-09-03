# coding: utf-8
from __future__ import unicode_literals

from django import template
from django.template.defaultfilters import stringfilter

try:
    from django_jinja import library
except ImportError:
    library = None

from ..utils import create_thumbs as _create_thumbs


# if django_jinja not installed - then use standart template
if library is None:
    register = template.Library()
else:
    register = library


@register.filter
@stringfilter
def create_thumbs(value):
    """
    Replace images by thumbs `on fly`
    """
    return _create_thumbs(value)
