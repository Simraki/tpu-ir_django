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


class RepresentativeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Representative
        fields = '__all__'


class AgreementSerializer(serializers.ModelSerializer):
    partner = PartnerSerializer(read_only=True, source='id_partner')
    company = CompanySerializer(read_only=True, source='id_partner__id_company')
    representative = RepresentativeSerializer(read_only=True, source='id_representative')

    class Meta:
        model = Agreement
        fields = '__all__'


class AgreementTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AgreementType
        fields = '__all__'
