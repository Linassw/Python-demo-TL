# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('currency_id', models.CharField(max_length=100)),
                ('available_supply', models.FloatField()),
                ('last_updated', models.TimeField()),
                ('market_cap_eur', models.FloatField()),
                ('market_cap_usd', models.FloatField()),
                ('max_supply', models.FloatField()),
                ('name', models.CharField(max_length=100)),
                ('percent_change_1h', models.FloatField()),
                ('percent_change_7d', models.FloatField()),
                ('percent_change_24h', models.FloatField()),
                ('price_btc', models.FloatField()),
                ('price_eur', models.FloatField()),
                ('price_usd', models.FloatField()),
                ('rank', models.IntegerField()),
                ('symbol', models.CharField(max_length=100)),
                ('total_supply', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Desktop',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('currency', models.ForeignKey(to='currencies.Currency')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
