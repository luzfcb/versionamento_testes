# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('um', '0002_auto_20150619_1312'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='um',
            options={'ordering': ['-id']},
        ),
        migrations.AlterField(
            model_name='um',
            name='versao',
            field=models.PositiveIntegerField(default=1),
        ),
    ]
