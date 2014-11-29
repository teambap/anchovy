# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('user_id', models.IntegerField(max_length=11)),
                ('name', models.CharField(max_length=200)),
                ('link', models.URLField()),
                ('registered', models.DateField()),
                ('updated', models.DateField()),
                ('status', models.CharField(max_length=2)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
