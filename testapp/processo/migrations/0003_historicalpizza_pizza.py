# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('processo', '0002_historicallivro'),
    ]

    operations = [
        migrations.CreateModel(
            name='HistoricalPizza',
            fields=[
                ('id', models.IntegerField(blank=True, auto_created=True, verbose_name='ID', db_index=True)),
                ('nome', models.CharField(max_length=128)),
                ('sabor', models.CharField(max_length=128)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(related_name='+', null=True, to=settings.AUTH_USER_MODEL, on_delete=django.db.models.deletion.SET_NULL)),
                ('modificado_por', models.ForeignKey(blank=True, related_name='+', null=True, to=settings.AUTH_USER_MODEL, on_delete=django.db.models.deletion.DO_NOTHING, db_constraint=False)),
            ],
            options={
                'get_latest_by': 'history_date',
                'ordering': ('-history_date', '-history_id'),
                'verbose_name': 'historical pizza',
            },
        ),
        migrations.CreateModel(
            name='Pizza',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('nome', models.CharField(max_length=128)),
                ('sabor', models.CharField(max_length=128)),
                ('modificado_por', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='+')),
            ],
        ),
    ]
