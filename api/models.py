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
    website = models.CharField(max_length=2048, null=True)
    id_country = models.ForeignKey(Country, models.DO_NOTHING, db_column='id_country')
    location = fields.ArrayField(models.FloatField(), size=2, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'Companies'


class AgreementType(models.Model):
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'AgreementTypes'


class Partner(models.Model):
    first_name = models.CharField(max_length=100)
    second_name = models.CharField(max_length=100)
    third_name = models.CharField(max_length=100, null=True)
    email = models.CharField(max_length=100, null=True)
    phone = models.CharField(max_length=50, null=True)
    id_company = models.ForeignKey(Company, models.DO_NOTHING, db_column='id_company')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'Partners'


class EngineeringSchool(models.Model):
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'EngineeringSchools'


class Representative(models.Model):
    first_name = models.CharField(max_length=100)
    second_name = models.CharField(max_length=100)
    third_name = models.CharField(max_length=100, null=True)
    email = models.CharField(max_length=100, null=True)
    phone = models.CharField(max_length=50, null=True)
    id_school = models.ForeignKey(EngineeringSchool, models.DO_NOTHING, db_column='id_school')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'Representatives'


class ResearchDomain(models.Model):
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'ResearchDomains'


class Status(models.Model):
    name = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'Status'


class Agreement(models.Model):
    name = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField(null=True)
    news_url = models.TextField(null=True)
    comments = models.TextField(null=True)
    id_agr_type = models.ForeignKey(AgreementType, models.DO_NOTHING,
                                    db_column='id_agrType')
    id_research_domain = models.ForeignKey(ResearchDomain, models.DO_NOTHING,
                                           db_column='id_researchDomain')
    id_representative = models.ForeignKey(Representative, models.DO_NOTHING, db_column='id_representative')
    id_partner = models.ForeignKey(Partner, models.DO_NOTHING, db_column='id_partner')
    id_status = models.ForeignKey(Status, models.DO_NOTHING, db_column='id_status')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'Agreements'

    def __str__(self):
        from django.core import serializers
        return serializers.serialize('json', [self, ])
