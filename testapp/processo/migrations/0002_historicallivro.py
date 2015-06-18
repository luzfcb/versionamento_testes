# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('processo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HistoricalLivro',
            fields=[
                ('id', models.IntegerField(auto_created=True, db_index=True, verbose_name='ID', blank=True)),
                ('criado_em', models.DateTimeField(editable=False, blank=True)),
                ('modificado_em', models.DateTimeField(editable=False, blank=True)),
                ('nome', models.CharField(max_length=128)),
                ('autor', models.CharField(max_length=128)),
                ('history_id', models.AutoField(serialize=False, primary_key=True)),
                ('history_date', models.DateTimeField()),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('criado_por', models.ForeignKey(related_name='+', to=settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=django.db.models.deletion.DO_NOTHING, db_constraint=False)),
                ('history_user', models.ForeignKey(related_name='+', to=settings.AUTH_USER_MODEL, null=True, on_delete=django.db.models.deletion.SET_NULL)),
                ('modificado_por', models.ForeignKey(related_name='+', to=settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=django.db.models.deletion.DO_NOTHING, db_constraint=False)),
            ],
            options={
                'verbose_name': 'historical livro',
                'get_latest_by': 'history_date',
                'ordering': ('-history_date', '-history_id'),
            },
        ),
    ]
