# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30, verbose_name=b'\xe5\xad\xa6\xe7\x94\x9f\xe5\xa7\x93\xe5\x90\x8d')),
                ('age', models.IntegerField(verbose_name=b'\xe5\xad\xa6\xe7\x94\x9f\xe5\xb9\xb4\xe9\xbe\x84')),
                ('gender', models.CharField(max_length=10, verbose_name=b'\xe5\xad\xa6\xe7\x94\x9f\xe6\x80\xa7\xe5\x88\xab')),
                ('major', models.CharField(max_length=30, verbose_name=b'\xe6\x89\x80\xe5\xad\xa6\xe4\xb8\x93\xe4\xb8\x9a')),
                ('nation', models.CharField(max_length=20, verbose_name=b'\xe6\xb0\x91\xe6\x97\x8f')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
