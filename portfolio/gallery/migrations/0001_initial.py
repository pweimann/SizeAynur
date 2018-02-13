# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-13 10:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailimages', '0019_delete_filter'),
        ('wagtailcore', '0040_page_draft_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='GalleryImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('image', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='+', to='wagtailimages.Image', verbose_name='image')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='GalleryPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('featured_image', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='wagtailimages.Image', verbose_name='featured image')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.AddField(
            model_name='galleryimage',
            name='page',
            field=modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.PROTECT, related_name='gallery_images', to='gallery.GalleryPage'),
        ),
    ]
