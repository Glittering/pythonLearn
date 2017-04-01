# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-01 09:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='people',
            name='age',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='people',
            name='contact_infor',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='people',
            name='describe',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='people',
            name='education',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='people',
            name='name',
            field=models.CharField(blank=True, max_length=4, null=True),
        ),
        migrations.AlterField(
            model_name='people',
            name='nation',
            field=models.CharField(blank=True, choices=[('han', '汉族'), ('hui', '回族'), ('man', '满族')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='people',
            name='nation_place',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='people',
            name='professional',
            field=models.CharField(blank=True, choices=[('english', '英语'), ('chinese', '汉语')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='people',
            name='sex',
            field=models.CharField(blank=True, choices=[('male', '男'), ('female', '女')], max_length=4, null=True),
        ),
    ]