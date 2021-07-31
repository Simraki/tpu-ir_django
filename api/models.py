from django.contrib.postgres import fields
from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'Countries'


class Company(models.Model):
    name = models.CharField(max_length=500)
    website = models.CharField(max_length=2048, blank=True, null=False)
    id_country = models.ForeignKey(Country, models.DO_NOTHING, db_column='id_country')
    location = fields.ArrayField(models.FloatField(), blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'Companies'
