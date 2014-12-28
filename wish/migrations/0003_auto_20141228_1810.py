# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wish', '0002_auto_20141129_1830'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='created',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='item',
            name='modified',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='item',
            name='user_id',
            field=models.IntegerField(),
        ),
    ]
