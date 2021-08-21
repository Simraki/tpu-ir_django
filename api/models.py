from django.contrib.auth import get_user_model
from django.contrib.postgres import fields
from django.db import models


# Reference tables

class AgreementType(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        db_table = 'AgreementTypes'


class EngineeringSchool(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        db_table = 'EngineeringSchools'


class ResearchDomain(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        db_table = 'ResearchDomains'


class Country(models.Model):
    name = models.CharField(max_length=200)
    code = models.IntegerField(null=True)

    class Meta:
        db_table = 'Countries'


class Status(models.Model):
    name = models.CharField(max_length=300)

    class Meta:
        db_table = 'Status'


# Operated models tables

class Company(models.Model):
    name = models.CharField(max_length=500)
    website = models.CharField(max_length=2048, blank=True, default='')
    id_country = models.ForeignKey(Country, models.DO_NOTHING, db_column='id_country')
    location = fields.ArrayField(models.FloatField(), size=2, default=list)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'Companies'


class Partner(models.Model):
    first_name = models.CharField(max_length=100)
    second_name = models.CharField(max_length=100)
    third_name = models.CharField(max_length=100, blank=True, default='')
    email = models.EmailField(max_length=100, blank=True, default='')
    phone = models.CharField(max_length=50, blank=True, default='')
    id_company = models.ForeignKey(Company, models.DO_NOTHING, db_column='id_company')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'Partners'


class Representative(models.Model):
    first_name = models.CharField(max_length=100)
    second_name = models.CharField(max_length=100)
    third_name = models.CharField(max_length=100, blank=True, default='')
    email = models.EmailField(max_length=100, blank=True, default='')
    phone = models.CharField(max_length=50, blank=True, default='')
    id_school = models.ForeignKey(EngineeringSchool, models.DO_NOTHING, db_column='id_school')
    id_user = models.ForeignKey(get_user_model(), models.DO_NOTHING, db_column='id_user', null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'Representatives'


class Agreement(models.Model):
    name = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField(null=True)
    news_url = fields.ArrayField(models.CharField(max_length=2048), default=list)
    comments = fields.ArrayField(models.CharField(max_length=2048), default=list)
    id_agr_type = models.ForeignKey(AgreementType, models.DO_NOTHING,
                                    db_column='id_agr_type')
    id_research_domain = models.ForeignKey(ResearchDomain, models.DO_NOTHING,
                                           db_column='id_research_domain')
    id_representative = models.ForeignKey(Representative, models.DO_NOTHING, db_column='id_representative')
    id_partner = models.ForeignKey(Partner, models.DO_NOTHING, db_column='id_partner')
    id_status = models.ForeignKey(Status, models.DO_NOTHING, db_column='id_status')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'Agreements'

    # def __str__(self):
    #     from django.core import serializers
    #     return serializers.serialize('json', [self, ])
