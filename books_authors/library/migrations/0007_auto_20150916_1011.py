# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0006_auto_20150916_0933'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='user',
            field=models.OneToOneField(related_name='reviews_by_user', to=settings.AUTH_USER_MODEL),
        ),
    ]
