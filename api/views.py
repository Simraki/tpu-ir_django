from datetime import timedelta

from django.db.models import BooleanField, Case, F, Q, Value, When
from django.http import JsonResponse
from django.utils import timezone
from django.utils.decorators import method_decorator
from drf_spectacular.openapi import OpenApiParameter, OpenApiTypes
from drf_spectacular.utils import extend_schema
from rest_framework import generics, viewsets

from validators import *
from .serializers import *


#
#   Country
#
class CountryView(viewsets.ReadOnlyModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer


#
#   Company
#
@method_decorator(name='list',
                  decorator=extend_schema(parameters=[OpenApiParameter(name='id_country', type=OpenApiTypes.INT),
                                                      OpenApiParameter(name='id_agreement_type', type=OpenApiTypes.INT,
                                                                       description="Может принимать более одного значения через запятую"),
                                                      OpenApiParameter(name='id_representative',
                                                                       type=OpenApiTypes.INT),
                                                      OpenApiParameter(name='id_school',
                                                                       type=OpenApiTypes.INT),
                                                      OpenApiParameter(name='state',
                                                                       type=OpenApiTypes.STR,
                                                                       enum=['active', 'expired', 'expiringSoon']),
                                                      ]))
class CompanyView(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    filter_fields = ['id_country']

    def get_queryset(self):
        list_id_types = self.request.query_params.get('id_agreement_type')
        list_id_types = list_id_types.split(',') if list_id_types else None

        list_state = self.request.query_params.get('state')
        list_state = list_state.split(',') if list_state else None

        id_representative = self.request.query_params.get('id_representative')
        id_school = self.request.query_params.get('id_school')

        allowed_state = ['Active', 'Expired', 'ExpiringSoon']
        if validate_list_enum(list_state, allowed_state):
            now = timezone.now()
            hopper = None
            for state in list_state:
                state = state.lower()
                if state == 'active':
                    if hopper is None:
                        hopper = Q(partner__agreement__end_date__isnull=True) | Q(partner__agreement__end_date__gte=now)
                    else:
                        hopper = hopper | \
                                 Q(partner__agreement__end_date__isnull=True) | \
                                 Q(partner__agreement__end_date__gte=now)
                elif state == 'expired':
                    if hopper is None:
                        hopper = Q(partner__agreement__end_date__lt=now)
                    else:
                        hopper = hopper | Q(partner__agreement__end_date__lt=now)
                elif state == 'expiringsoon':
                    if hopper is None:
                        hopper = Q(partner__agreement__end_date__range=[now, now + timedelta(days=182)])
                    else:
                        hopper = hopper | Q(partner__agreement__end_date__range=[now, now + timedelta(days=182)])

            self.queryset = self.queryset.filter(hopper)
        if validate_int(id_representative, min_value=0):
            self.queryset = self.queryset.filter(partner__agreement__id_representative=id_representative)
        if validate_list_int(list_id_types, min_value=0):
            self.queryset = self.queryset.filter(partner__agreement__id_agr_type__in=list_id_types)
        if validate_int(id_school, min_value=0):
            self.queryset = self.queryset.filter(partner__agreement__id_representative__id_school=id_school)

        return self.queryset.distinct()


#
#   Agreement Type
#
class AgreementTypeView(viewsets.ModelViewSet):
    queryset = AgreementType.objects.all()
    serializer_class = AgreementTypeSerializer


#
#   Agreement
#
@method_decorator(name='list',
                  decorator=extend_schema(parameters=[OpenApiParameter(name='id_company', type=OpenApiTypes.INT)]))
class AgreementView(viewsets.ModelViewSet):
    queryset = Agreement.objects.all()
    serializer_class = AgreementSerializer

    def get_queryset(self):
        id_company = self.request.query_params.get('id_company')
        if validate_int(id_company, min_value=0):
            self.queryset = self.queryset.filter(id_partner__id_company=id_company)
        return self.queryset


#
#   Representative
#
class RepresentativeView(viewsets.ModelViewSet):
    queryset = Representative.objects.all()
    serializer_class = RepresentativeSerializer


#
#   Engineering School
#
class EngineeringSchoolView(viewsets.ModelViewSet):
    queryset = EngineeringSchool.objects.all()
    serializer_class = EngineeringSchoolSerializer


#
#   KPI
#
class KPIView(generics.ListAPIView):
    serializer_class = KPISerializer

    def list(self, request, *args, **kwargs):
        payload = {
            "countries_num": Country.objects.filter(company__partner__agreement__isnull=False).distinct().count(),
            "annual_agreements_num": Agreement.objects.filter(start_date__year=2021).count(),
            "companies_num": Company.objects.count(),
            "researches_num": Agreement.objects.filter(id_agr_type=4).count()
        }

        data = self.get_serializer(payload).data

        return JsonResponse(data, status=200)


#
#   Company Timeline
#
class CompanyTimelineView(generics.ListAPIView):
    serializer_class = CompanyTimelineSerializer

    def list(self, request, *args, **kwargs):
        hopper = Q(end_date__isnull=True) | Q(end_date__gt=timezone.now())

        queryset = Agreement.objects.filter(id_partner__id_company=kwargs['pk']).select_related('id_agr_type') \
            .annotate(agr_type_name=F('id_agr_type__name'),
                      is_active=Case(When(hopper, then=Value(True)), default=Value(False),
                                     output_field=BooleanField())
                      )

        output = []

        for q in queryset:
            output.append({
                'id_agreement': q.pk,
                'agr_type_name': q.agr_type_name,
                'is_active': q.is_active,
                'is_end_date': False,
                'date': q.start_date
            })
            if q.end_date:
                output.append({
                    'id_agreement': q.pk,
                    'agr_type_name': q.agr_type_name,
                    'is_active': q.is_active,
                    'is_end_date': True,
                    'date': q.end_date
                })

        output.sort(key=lambda x: x['date'])

        data = self.get_serializer(output, many=True).data

        return JsonResponse(data, status=200, safe=False)
