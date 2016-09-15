# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bulletin',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('theLine', models.TextField(unique=True)),
                ('theLink', models.URLField(unique=True)),
                ('subjectsTo', models.PositiveIntegerField(choices=[(0, b'Branch'), (1, b'Sectional'), (2, b'Regional'), (3, b'Interregional'), (4, b'Misc')])),
            ],
        ),
        migrations.CreateModel(
            name='Events',
            fields=[
                ('eventID', models.CharField(max_length=7, serialize=False, primary_key=True)),
                ('regLink', models.URLField(unique=True)),
                ('deadLine', models.DateField()),
                ('eventDate', models.DateField()),
                ('fbLink', models.URLField()),
                ('ag', models.PositiveIntegerField(choices=[(0, b'None'), (1, b'Computer Society'), (2, b'WIE'), (4, b'Focus Group')])),
                ('info', models.TextField()),
                ('requirements', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('ieee_num', models.PositiveIntegerField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=40)),
            ],
        ),
    ]
