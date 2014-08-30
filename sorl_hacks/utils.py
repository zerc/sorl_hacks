# coding: utf-8
from __future__ import unicode_literals

import os
import re

from sorl.thumbnail import get_thumbnail
from django.conf import settings


URLS_RE = re.compile(
    r'src="(.*?)" style=".*?height:(\d+)px;.*?width:(\d+)px',
    re.I | re.U | re.M)


def create_thumbs(value):
    """
    Parse given html string for search img tag
    with height and width styles
    """
    chunks = URLS_RE.findall(value)

    if not chunks:
        return value

    for chunk in chunks:
        if len(chunk) != 3:
            continue

        url, height, width = chunk

        img_path = os.path.join(settings.BASE_DIR, url[url.startswith('/'):])
        thumb = get_thumbnail(img_path, '{}x{}'.format(width, height))

        value = value.replace(url, thumb.url)

    return value
