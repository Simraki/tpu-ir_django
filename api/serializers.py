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


class EngineeringSchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = EngineeringSchool
        fields = '__all__'


class AgreementTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AgreementType
        fields = '__all__'


class AgreementSerializer(serializers.ModelSerializer):
    partner = PartnerSerializer(read_only=True, source='id_partner')
    company = CompanySerializer(read_only=True, source='id_partner__id_company')
    representative = RepresentativeSerializer(read_only=True, source='id_representative')
    agreement_type = AgreementTypeSerializer(read_only=True, source='id_agr_type')

    class Meta:
        model = Agreement
        fields = '__all__'


class KPISerializer(serializers.Serializer):
    countries_num = serializers.IntegerField(min_value=0)
    annual_agreements_num = serializers.IntegerField(min_value=0)
    companies_num = serializers.IntegerField(min_value=0)
    researches_num = serializers.IntegerField(min_value=0)


class CompanyTimelineSerializer(serializers.Serializer):
    id_agreement = serializers.IntegerField(min_value=0)
    agr_type_name = serializers.CharField(max_length=200)
    is_active = serializers.BooleanField()
    is_end_date = serializers.BooleanField()
    date = serializers.DateField()
