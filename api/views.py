from django.http import JsonResponse
from django.utils.decorators import method_decorator
from drf_spectacular.openapi import OpenApiParameter, OpenApiTypes
from drf_spectacular.utils import extend_schema
from rest_framework import viewsets

from validators import *
from .serializers import *


class CountryView(viewsets.ReadOnlyModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer


@method_decorator(name='list',
                  decorator=extend_schema(parameters=[OpenApiParameter(name='id_country', type=OpenApiTypes.INT),
                                                      OpenApiParameter(name='id_agreement_type', type=OpenApiTypes.INT,
                                                                       description="Может принимать более одного значения через запятую"),
                                                      OpenApiParameter(name='id_representative',
                                                                       type=OpenApiTypes.INT)]))
class CompanyView(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    filter_fields = ['id_country']

    def get_queryset(self):
        list_id_types = self.request.query_params.get('id_agreement_type')
        list_id_types = list_id_types.split(',') if list_id_types else None

        id_representative = self.request.query_params.get('id_representative')

        if validate_int(id_representative, min_value=0):
            self.queryset = self.queryset.filter(partner__agreement__id_representative=id_representative)
        if validate_list_int(list_id_types, min_value=0):
            self.queryset = self.queryset.filter(partner__agreement__id_agr_type__in=list_id_types)

        return self.queryset.distinct()


class AgreementTypeView(viewsets.ModelViewSet):
    queryset = AgreementType.objects.all()
    serializer_class = AgreementTypeSerializer


@method_decorator(name='list',
                  decorator=extend_schema(parameters=[OpenApiParameter(name='id_company', type=OpenApiTypes.INT)]))
class AgreementView(viewsets.ModelViewSet):
    queryset = Agreement.objects.all()
    serializer_class = AgreementSerializer

    def get_queryset(self):
        id_company = self.request.query_params.get('id_company')
        if id_company is not None and int(id_company) > 0:
            return self.queryset.filter(id_partner__id_company=id_company).all()
        return self.queryset


class RepresentativeView(viewsets.ModelViewSet):
    queryset = Representative.objects.all()
    serializer_class = RepresentativeSerializer


class KPIView(viewsets.GenericViewSet):

    def list(self, request):
        payload = {
            "countries_num": Country.objects.filter(company__partner__agreement__isnull=False).order_by(
                    'id').distinct().count(),
            "annual_agreements_num": Agreement.objects.filter(start_date__year=2021).count(),
            "companies_num": Company.objects.count(),
            "researches_num": Agreement.objects.filter(id_agr_type=4).count()
        }

        return JsonResponse(payload, status=200)
