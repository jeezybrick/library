# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='rate',
        ),
        migrations.AddField(
            model_name='book',
            name='rate',
            field=models.PositiveIntegerField(default=0, choices=[(0, b'0'), (1, b'1'), (2, b'2'), (3, b'3'), (4, b'4'), (5, b'5')]),
        ),
        migrations.AddField(
            model_name='book',
            name='votes',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
