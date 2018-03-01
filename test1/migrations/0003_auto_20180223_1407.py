# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('test1', '0002_auto_20180222_1235'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='ushou',
            field=models.CharField(default=b'', max_length=20),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='uaddress',
            field=models.CharField(default=b'', max_length=100),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='uemail',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='upwd',
            field=models.CharField(max_length=40),
        ),
    ]
