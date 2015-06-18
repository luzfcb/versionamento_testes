# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import versionfield


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ImpliUm',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('texto', models.TextField()),
                ('versao', versionfield.VersionField()),
            ],
        ),
    ]
