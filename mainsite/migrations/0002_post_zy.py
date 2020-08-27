# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='zy',
            field=models.CharField(max_length=200, default=''),
            preserve_default=False,
        ),
    ]
