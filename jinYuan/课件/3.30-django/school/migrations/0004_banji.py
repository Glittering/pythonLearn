# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0003_student'),
    ]

    operations = [
        migrations.CreateModel(
            name='Banji',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('teacher', models.ForeignKey(to='school.Teacher')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
