# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='teacher',
            options={'verbose_name_plural': '\u6559\u5e08\u8868'},
        ),
        migrations.AlterField(
            model_name='teacher',
            name='age',
            field=models.IntegerField(null=True, verbose_name=b'\xe6\x95\x99\xe5\xb8\x88\xe5\xb9\xb4\xe9\xbe\x84', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='teacher',
            name='date',
            field=models.DateField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='teacher',
            name='img',
            field=models.ImageField(upload_to=b'image', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='teacher',
            name='name',
            field=models.CharField(max_length=30, verbose_name=b'\xe6\x95\x99\xe5\xb8\x88\xe5\xa7\x93\xe5\x90\x8d'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='teacher',
            name='subject',
            field=models.CharField(max_length=40, verbose_name=b'\xe6\x95\x99\xe6\x8e\x88\xe7\xa7\x91\xe7\x9b\xae'),
            preserve_default=True,
        ),
    ]
