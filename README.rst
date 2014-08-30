django-sorl-hacks
==================

Template tag **create_thumbs** - parsing your text on fly, finds images urls and replace by thumb url:

::

    {% load sorl_hacks %}

    {% for text_block in post.blocks.all %}
        <h4>{{ text_block }}</h4>
        <p>{{ text_block.body|create_thumbs|safe }}</p>
        <hr>
    {% endfor %}



**ThumbedCkeditorImages** admin model mixin with post_save replacing.

admin.py:

.. code:: python
    
    from sorl_hacks.admin import ThumbedCkeditorImages

    class BlogPostAdmin(ThumbedCkeditorImages):
        ...

