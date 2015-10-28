# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chronic_medicare', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChronicConditionRegression',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('features', models.CharField(max_length=512)),
                ('target', models.CharField(max_length=512)),
                ('analysis_type', models.CharField(max_length=512)),
                ('description', models.TextField(blank=True, max_length=2048)),
                ('summary_html', models.CharField(blank=True, max_length=8192)),
                ('plot_html', models.CharField(blank=True, max_length=8388608)),
                ('aic', models.FloatField(blank=True, max_length=64, null=True)),
                ('bic', models.FloatField(blank=True, max_length=64, null=True)),
                ('num_observations', models.IntegerField(blank=True, null=True)),
                ('df_residuals', models.IntegerField(blank=True, null=True)),
                ('r_squared', models.FloatField(blank=True, max_length=64, null=True)),
                ('r_squared_adjusted', models.FloatField(blank=True, max_length=64, null=True)),
                ('f_statistic', models.FloatField(blank=True, max_length=64, null=True)),
                ('jarque_bera', models.FloatField(blank=True, max_length=64, null=True)),
                ('jarque_bera_prob', models.FloatField(blank=True, max_length=64, null=True)),
                ('skew', models.FloatField(blank=True, max_length=64, null=True)),
                ('kurtosis', models.FloatField(blank=True, max_length=64, null=True)),
                ('source_file', models.ForeignKey(to='chronic_medicare.AnalysisFile', related_name='regressions')),
            ],
        ),
    ]
