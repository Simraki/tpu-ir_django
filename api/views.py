from django.utils.decorators import method_decorator
from drf_spectacular.openapi import OpenApiTypes, OpenApiParameter
from drf_spectacular.utils import extend_schema
from rest_framework import viewsets

from api.models import *
from . import serializers


class CountryView(viewsets.ReadOnlyModelViewSet):
    queryset = Country.objects.order_by('name')
    serializer_class = serializers.CountrySerializer


@method_decorator(name='list',
                  decorator=extend_schema(parameters=[OpenApiParameter(name='id_country', type=OpenApiTypes.INT),
                                                      OpenApiParameter(name='id_agreement_type', type=OpenApiTypes.INT),
                                                      OpenApiParameter(name='id_delegate', type=OpenApiTypes.INT)]))
class CompanyView(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = serializers.CompanySerializer
    filter_fields = ['id_country']

    def get_queryset(self):
        id_type = self.request.query_params.get('id_agreement_type', -1)
        if id_type is not None and int(id_type) > 0:
            return Company.objects.filter(partner__agreement__id_agr_type=id_type)

        id_delegate = self.request.query_params.get('id_delegate', -1)
        if id_delegate is not None and int(id_delegate) > 0:
            return Company.objects.filter(partner__agreement__id_representative=id_delegate)

        return self.queryset


class AgreementTypeView(viewsets.ModelViewSet):
    queryset = AgreementType.objects.all()
    serializer_class = serializers.AgreementTypeSerializer


@method_decorator(name='list',
                  decorator=extend_schema(parameters=[OpenApiParameter(name='id_company', type=OpenApiTypes.INT)]))
class AgreementView(viewsets.ModelViewSet):
    queryset = Agreement.objects.order_by('start_date')
    serializer_class = serializers.AgreementSerializer

    def get_queryset(self):
        id_company = self.request.query_params.get('id_company')
        if id_company is not None and int(id_company) > 0:
            return self.queryset.filter(id_partner__id_company=id_company).order_by('start_date')
        return self.queryset


class RepresentativeView(viewsets.ModelViewSet):
    queryset = Representative.objects.all()
    serializer_class = serializers.RepresentativeSerializer
