# coding: utf-8
from __future__ import unicode_literals

import os
import re

from sorl.thumbnail import get_thumbnail
from django.conf import settings

flags = re.I | re.U | re.M

URLS_RE = re.compile(r'src="(.*?)" style="(.*?)"', flags)
WIDTH_RE = re.compile(r'width:\s*?(\d+)px', flags)
HEIGHT_RE = re.compile(r'height:\s*?(\d+)px', flags)


def create_thumbs(value):
    """
    Parse given html string for search img tag
    with height and width styles
    """
    chunks = URLS_RE.findall(value)

    if not chunks:
        return value

    for chunk in chunks:
        if len(chunk) != 2:
            continue

        wh = parse_style(chunk[-1])

        if not wh:
            continue

        url, width, height = chunk[0], wh[0], wh[1]

        img_path = os.path.join(settings.BASE_DIR, url[url.startswith('/'):])
        thumb = get_thumbnail(img_path, '{}x{}'.format(width, height))

        value = value.replace(url, thumb.url)

    return value


def parse_style(style_string):
    """
    Parse style attribute of img tag
    Return tuple like (width, height) or None
    """
    try:
        return (WIDTH_RE.findall(style_string)[0],
                HEIGHT_RE.findall(style_string)[0])
    except IndexError:
        return None
