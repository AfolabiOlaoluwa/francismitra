# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=250)),
                ('content', models.TextField(null=True, blank=True)),
                ('sorter', models.IntegerField(default=0)),
                ('slug', models.SlugField()),
            ],
            options={
                'verbose_name_plural': 'categories',
            },
        ),
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=250)),
                ('caption', models.CharField(max_length=250, null=True, blank=True)),
                ('year', models.CharField(max_length=4, null=True, blank=True)),
                ('photo', models.ImageField(upload_to=b'portfolio/')),
                ('category', models.ForeignKey(to='portfolio.Categories')),
            ],
            options={
                'verbose_name_plural': 'images',
            },
        ),
        migrations.CreateModel(
            name='Videos',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=250)),
                ('caption', models.CharField(max_length=250, null=True, blank=True)),
                ('year', models.CharField(max_length=4, null=True, blank=True)),
                ('provider', models.CharField(max_length=2, choices=[(b'YU', b'YouTube'), (b'VI', b'Vimeo')])),
                ('url', models.CharField(max_length=250)),
                ('category', models.ForeignKey(to='portfolio.Categories')),
            ],
            options={
                'verbose_name_plural': 'videos',
            },
        ),
    ]
