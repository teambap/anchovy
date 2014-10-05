# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('user_id', models.CharField(max_length=20)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Kakao',
            fields=[
                ('user_ptr', models.OneToOneField(serialize=False, primary_key=True, to='users.User', auto_created=True, parent_link=True)),
                ('kakao_id', models.CharField(max_length=30)),
                ('nickname', models.CharField(max_length=30)),
                ('profile_image', models.CharField(max_length=100)),
                ('thumbnail_image', models.CharField(max_length=100)),
            ],
            options={
            },
            bases=('users.user',),
        ),
    ]
