# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import versionfield


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Um',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('texto', models.TextField()),
                ('versao', versionfield.VersionField()),
            ],
        ),
    ]
