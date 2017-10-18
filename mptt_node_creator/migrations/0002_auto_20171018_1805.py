# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mptt_node_creator', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='examplenodecreaterequest',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Create date', null=True),
        ),
        migrations.AddField(
            model_name='examplenodecreaterequest',
            name='is_request_to_add',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='examplenodecreaterequest',
            name='requester',
            field=models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AlterField(
            model_name='examplenodecreaterequest',
            name='parent',
            field=models.ForeignKey(blank=True, to='mptt_node_creator.ExampleNodeCreateRequest', null=True),
        ),
    ]
