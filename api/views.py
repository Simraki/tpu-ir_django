from rest_framework import viewsets

from api.models import *
from . import serializers


class CountryView(viewsets.ReadOnlyModelViewSet):
    queryset = Country.objects.all()
    serializer_class = serializers.CountrySerializer


class CompanyView(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = serializers.CompanySerializer
