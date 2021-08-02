# Generated by Django 3.2 on 2021-08-01 20:12

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='location',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(), blank=True, null=True, size=2),
        ),
        migrations.AlterField(
            model_name='company',
            name='website',
            field=models.CharField(max_length=2048),
        ),
    ]
