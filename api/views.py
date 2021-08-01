from rest_framework import viewsets
from url_filter.integrations.drf import DjangoFilterBackend

from api.models import *
from . import serializers


class CountryView(viewsets.ReadOnlyModelViewSet):
    queryset = Country.objects.order_by('name')
    serializer_class = serializers.CountrySerializer


class CompanyView(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = serializers.CompanySerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['id_country']
