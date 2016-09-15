# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('parent', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='events',
            name='eventName',
            field=models.CharField(default=b'Suggest', max_length=12),
        ),
        migrations.AddField(
            model_name='events',
            name='venue',
            field=models.CharField(default=b'To be updated', max_length=20),
        ),
        migrations.AddField(
            model_name='user',
            name='isCS',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='memCSExpires',
            field=models.DateField(default=datetime.datetime(2016, 7, 25, 5, 45, 18, 262493, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='memExpires',
            field=models.DateField(default=datetime.datetime(2016, 7, 25, 5, 45, 24, 758124, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
