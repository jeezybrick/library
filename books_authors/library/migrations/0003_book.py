# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0002_genre'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255)),
                ('annotation', models.TextField()),
                ('slug', models.SlugField(unique=True)),
                ('author', models.ForeignKey(to='library.Author')),
                ('genre', models.ManyToManyField(to='library.Genre')),
            ],
        ),
    ]
