# coding: utf-8
from __future__ import unicode_literals

from django import template
from django.template.defaultfilters import stringfilter

from ..utils import create_thumbs as _create_thumbs


register = template.Library()


@register.filter
@stringfilter
def create_thumbs(value):
    """
    Replace images by thumbs `on fly`
    """
    return _create_thumbs(value)
