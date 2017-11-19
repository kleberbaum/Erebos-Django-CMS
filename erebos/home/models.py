from __future__ import absolute_import, unicode_literals

from django.db import models

from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.fields import StreamField, RichTextField
from wagtail.wagtailcore import blocks
from wagtail.wagtailadmin.edit_handlers import TabbedInterface, ObjectList, InlinePanel, StreamFieldPanel, MultiFieldPanel, FieldPanel
from wagtail.wagtailimages.blocks import ImageChooserBlock


class HomePage(Page):
    header = StreamField([
        ('hbanner', blocks.StructBlock([
            ('banner', blocks.CharBlock(blank=True, classname="full title", icon='title'))
        ], required=False, icon='bold')),

        ('hfull', blocks.StructBlock([
            ('full', blocks.CharBlock(blank=True, classname="full title", icon='title'))
        ], required=False, icon='placeholder')),

        ('hcode', blocks.StructBlock([
            ('code', blocks.RawHTMLBlock(blank=True, classname="full"))
        ], icon='code'))
    ], blank=True)

    article = StreamField([
        ('aabout', blocks.StructBlock([
            ('about_pages', blocks.StreamBlock([
                ('about', blocks.StructBlock([
                    ('blink', blocks.CharBlock(blank=True, classname="full")),
                    ('use_image', blocks.BooleanBlock(default=False, help_text="Use picture instead of blink", required=False, classname="full")),
                    ('image', ImageChooserBlock(required=False, classname="full")),
                    ('boxes', blocks.StreamBlock([
                        ('title', blocks.CharBlock(blank=True, classname="full title", icon='title')),
                        ('content', blocks.RichTextBlock(blank=True, classname="full"))
                    ]))
                ], icon='doc-full'))
            ], icon='cogs')),
        ], icon='radio-empty')),

        ('amotd', blocks.StructBlock([
            ('modt', blocks.CharBlock(max_length=16, default="Sky's The Limit", classname="full")),
        ], icon='pilcrow')),

        ('asharingan', blocks.StructBlock([
            ('sharingan', blocks.StructBlock([
                ('sharingan_1', blocks.RichTextBlock(default="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.", classname="full")),
                ('sharingan_2', blocks.RichTextBlock(default="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.", classname="full")),
                ('sharingan_3', blocks.RichTextBlock(default="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.", classname="full")),

                ('nyan_titel', blocks.CharBlock(max_length=16, default="The Team", classname="full")),
                ('show_team', blocks.BooleanBlock(default=False, help_text="Whether team block will be shown on page", required=False, classname="full")),
                ('team', blocks.StreamBlock([
                    ('member', blocks.StructBlock([
                        ('pic', ImageChooserBlock(blank=True, classname="full")),
                        ('name', blocks.CharBlock(blank=True, max_length=16, default="", classname="full")),
                        ('description', blocks.CharBlock(max_length=128, default="", classname="full"))
                    ], icon='user'))
                ], required=False))
            ]))
        ], icon='view')),

        ('aspaceship', blocks.StructBlock([
        ], icon='pick')),

        ('agallery', blocks.StructBlock([
            ('title', blocks.CharBlock(blank=True, classname="full")),
            ('gallery', blocks.StreamBlock([
                ('image', ImageChooserBlock(blank=True, classname="full")),
            ]))
        ], icon='grip')),

        ('acode', blocks.StructBlock([
            ('code', blocks.RawHTMLBlock(blank=True, classname="full"))
        ], icon='code'))
    ], blank=True)



    main_content_panels = [
        StreamFieldPanel('header'),
        StreamFieldPanel('article')
    ]

    edit_handler = TabbedInterface([
        ObjectList(Page.content_panels + main_content_panels, heading='Main'),
        ObjectList(Page.promote_panels + Page.settings_panels, heading='Settings', classname="settings")
    ])
