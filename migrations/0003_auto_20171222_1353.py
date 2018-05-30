# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('currencies', '0002_auto_20171222_1229'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='desktop',
            name='currency',
        ),
        migrations.RemoveField(
            model_name='desktop',
            name='user',
        ),
        migrations.AddField(
            model_name='currency',
            name='users',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Desktop',
        ),
    ]
