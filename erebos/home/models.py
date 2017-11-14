from __future__ import absolute_import, unicode_literals

from django.db import models

from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.fields import StreamField, RichTextField
from wagtail.wagtailcore import blocks
from wagtail.wagtailadmin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.wagtailimages.blocks import ImageChooserBlock


class HomePage(Page):
    modt = models.CharField(max_length=16, default="")

    sh1 = RichTextField()
    sh2 = RichTextField()
    sh3 = RichTextField()

    about1 =  StreamField([
        ('title', blocks.CharBlock(classname="full title")),
        ('content', blocks.RichTextBlock()),
    ])

    about2 =  StreamField([
        ('title', blocks.CharBlock(classname="full title")),
        ('content', blocks.RichTextBlock()),
    ])

    about3 =  StreamField([
        ('title', blocks.CharBlock(classname="full title")),
        ('content', blocks.RichTextBlock()),
    ])

    about4 =  StreamField([
        ('title', blocks.CharBlock(classname="full title")),
        ('content', blocks.RichTextBlock()),
    ])

    about5 =  StreamField([
        ('title', blocks.CharBlock(classname="full title")),
        ('content', blocks.RichTextBlock()),
    ])

    about6 =  StreamField([
        ('title', blocks.CharBlock(classname="full title")),
        ('content', blocks.RichTextBlock()),
    ])

    nyan = models.CharField(max_length=16, default="")

    content_panels = Page.content_panels + [
            FieldPanel('modt', classname="full"),

            StreamFieldPanel('about1'),
            StreamFieldPanel('about2'),
            StreamFieldPanel('about3'),
            StreamFieldPanel('about4'),
            StreamFieldPanel('about5'),
            StreamFieldPanel('about6'),

            FieldPanel('sh1', classname="full"),
            FieldPanel('sh2', classname="full"),
            FieldPanel('sh3', classname="full"),

            FieldPanel('nyan', classname="full"),
        ]
