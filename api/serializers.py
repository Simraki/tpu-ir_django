from rest_framework import serializers

from .models import *


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'


class PartnerSerializer(serializers.ModelSerializer):
    company = CompanySerializer(read_only=True, source='id_company')

    class Meta:
        model = Partner
        fields = '__all__'


class AgreementSerializer(serializers.ModelSerializer):
    partner = PartnerSerializer(read_only=True, source='id_partner')

    class Meta:
        model = Agreement
        fields = '__all__'
