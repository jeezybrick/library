# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0005_auto_20150915_1305'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='written_by',
            new_name='user',
        ),
    ]
