==================
django-sorl-hacks
==================

create_thumbs template tag
--------------------------
Parse your text on fly, finds images urls and replace it by thumb url:

::

    {% load sorl_hacks %}

    {% for text_block in post.blocks.all %}
        <h4>{{ text_block }}</h4>
        <p>{{ text_block.body|create_thumbs|safe }}</p>
        <hr>
    {% endfor %}



ThumbedCkeditorImages
---------------------

Admin model mixin with post_save replacing.

admin.py:

.. code:: python

    from sorl_hacks.admin import ThumbedCkeditorImages

    class BlogPostAdmin(ThumbedCkeditorImages):
        ...


ThumbMixin
-----------
Usefull in stadart Django templates. Add property ``my_model.get_thumb_WIDTHxHEIGHT`` to yours models.

Example of ``my_model_detail.html``:

::

    {{ my_model.get_thumb_200x200.html }}

    {{ my_model.get_thumb_small.html }}


instead of:

::

    {% thumbnail my_model.pic "56x56" crop="center" as im %}
        <img src="{{ im.url }}" width="56" height="56">
    {% empty %}
        <img src="{{ MISSING_IMAGE }}" width="56" height="56">
    {% endthumbnail %}


**INSTALL**

Your ``models.py``:

.. code:: python

    from django.db import models
    from sorl.thumbnail import ImageField
    from sorl_hacks.models import ThumbMixin

    class Post(ThumbMixin, models.Model):
        image = ImageField('image', upload_to='posts', **nullable)
