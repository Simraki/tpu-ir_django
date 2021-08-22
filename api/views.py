from django.utils.decorators import method_decorator
from drf_spectacular.openapi import OpenApiTypes, OpenApiParameter
from drf_spectacular.utils import extend_schema
from rest_framework import viewsets

from api.models import *
from validators import *
from . import serializers


class CountryView(viewsets.ReadOnlyModelViewSet):
    queryset = Country.objects.all()
    serializer_class = serializers.CountrySerializer


@method_decorator(name='list',
                  decorator=extend_schema(parameters=[OpenApiParameter(name='id_country', type=OpenApiTypes.INT,
                                                                       description="Может принимать более одного значения через запятую"),
                                                      OpenApiParameter(name='id_agreement_type', type=OpenApiTypes.INT),
                                                      OpenApiParameter(name='id_representative',
                                                                       type=OpenApiTypes.INT)]))
class CompanyView(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = serializers.CompanySerializer
    filter_fields = ['id_country']

    def get_queryset(self):
        list_id_types = self.request.query_params.get('id_agreement_type').split(',')
        id_representative = self.request.query_params.get('id_representative')
        if validate_int(id_representative, min_value=0):
            self.queryset = self.queryset.filter(partner__agreement__id_representative=id_representative)
        if validate_list_int(list_id_types, min_value=0):
            self.queryset = self.queryset.filter(partner__agreement__id_agr_type__in=list_id_types)

        return self.queryset.distinct()


class AgreementTypeView(viewsets.ModelViewSet):
    queryset = AgreementType.objects.all()
    serializer_class = serializers.AgreementTypeSerializer


@method_decorator(name='list',
                  decorator=extend_schema(parameters=[OpenApiParameter(name='id_company', type=OpenApiTypes.INT)]))
class AgreementView(viewsets.ModelViewSet):
    queryset = Agreement.objects.all()
    serializer_class = serializers.AgreementSerializer

    def get_queryset(self):
        id_company = self.request.query_params.get('id_company')
        if id_company is not None and int(id_company) > 0:
            return self.queryset.filter(id_partner__id_company=id_company).all()
        return self.queryset


class RepresentativeView(viewsets.ModelViewSet):
    queryset = Representative.objects.all()
    serializer_class = serializers.RepresentativeSerializer
