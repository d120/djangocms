# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0016_auto_20160608_1535'),
    ]

    operations = [
        migrations.CreateModel(
            name='MenuEntryHeadlineExtension',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('headline', models.CharField(verbose_name='Menu entry headline', max_length=64, blank=True)),
                ('extended_object', models.OneToOneField(editable=False, to='cms.Title')),
                ('public_extension', models.OneToOneField(editable=False, null=True, related_name='draft_extension', to='d120.MenuEntryHeadlineExtension')),
            ],
            options={
                'verbose_name_plural': 'Menu Entry Headlines',
                'verbose_name': 'Menu Entry Headline',
            },
        ),
        migrations.CreateModel(
            name='MenuEntryMarginExtension',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('additional_margin', models.BooleanField(default=False, verbose_name='Enable additional margin for menu entry')),
                ('extended_object', models.OneToOneField(editable=False, to='cms.Page')),
                ('public_extension', models.OneToOneField(editable=False, null=True, related_name='draft_extension', to='d120.MenuEntryMarginExtension')),
            ],
            options={
                'verbose_name_plural': 'Menu Entry Margins',
                'verbose_name': 'Menu Entry Margin',
            },
        ),
        migrations.CreateModel(
            name='PageColorExtension',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('color', models.CharField(choices=[('#d35400', 'Orange'), ('#c0392b', 'Red'), ('#8e44ad', 'Purple'), ('#2980b9', 'Blue'), ('#16a085', 'Turquoise'), ('#27ae60', 'Green')], verbose_name='Color', max_length=16, blank=True)),
                ('extended_object', models.OneToOneField(editable=False, to='cms.Page')),
                ('public_extension', models.OneToOneField(editable=False, null=True, related_name='draft_extension', to='d120.PageColorExtension')),
            ],
            options={
                'verbose_name_plural': 'Page Colors',
                'verbose_name': 'Page Color',
            },
        ),
    ]
