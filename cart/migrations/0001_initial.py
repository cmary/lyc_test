# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0001_initial'),
        ('test1', '0003_auto_20180223_1407'),
    ]

    operations = [
        migrations.CreateModel(
            name='CartInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('count', models.IntegerField(default=0)),
                ('goods', models.ForeignKey(to='index.GoodsInfo')),
                ('user', models.ForeignKey(to='test1.UserInfo')),
            ],
        ),
    ]
