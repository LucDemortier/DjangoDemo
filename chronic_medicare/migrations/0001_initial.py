# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AnalysisFile',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=512)),
                ('csv_file', models.FileField(upload_to='analysis-files/')),
                ('description', models.TextField(max_length=1024, blank=True)),
            ],
            options={
                'verbose_name_plural': 'Raw Analysis Files',
            },
        ),
    ]
