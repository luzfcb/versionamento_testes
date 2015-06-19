# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dois',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('texto', models.TextField()),
                ('versao', models.PositiveIntegerField(default=1)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
    ]
