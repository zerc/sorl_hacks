# coding: utf-8
from __future__ import unicode_literals

from django.contrib import admin
from sorl_hacks.admin import ThumbedCkeditorImages

from .models import BlogPost, TextBlock, Tag


class TextBlockInline(admin.TabularInline):
    model = TextBlock
    extra = 1


class BlogPostAdmin(ThumbedCkeditorImages):
    list_display = ('title', 'category',)
    fields = ('title', 'category', 'image', 'tags', 'lead', 'body')
    list_select_related = ('category',)
    inlines = [TextBlockInline]
    filter_horizontal = ('tags',)


admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register([Tag])
