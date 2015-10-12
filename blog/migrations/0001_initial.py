# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PostImages',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('photo', models.ImageField(upload_to=b'blog/')),
            ],
            options={
                'verbose_name_plural': 'postimages',
            },
        ),
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=250, null=True, blank=True)),
                ('content', models.TextField(null=True, blank=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('category', models.CharField(max_length=2, choices=[(b'TU', b'Tutorials'), (b'DE', b'Default')])),
                ('slug', models.SlugField()),
            ],
            options={
                'verbose_name_plural': 'posts',
            },
        ),
        migrations.AddField(
            model_name='postimages',
            name='post',
            field=models.ForeignKey(to='blog.Posts'),
        ),
    ]
