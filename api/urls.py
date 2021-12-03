from django.urls import path
from rest_framework import routers

from .views import *

router = routers.DefaultRouter()
router.register(r'countries', CountryView)
router.register(r'companies', CompanyView)
router.register(r'agreements', AgreementView)
router.register(r'representatives', RepresentativeView)
router.register(r'agreement_types', AgreementTypeView)
router.register(r'schools', EngineeringSchoolView)

urlpatterns = router.urls + [
    path(r'timeline/<int:pk>/', CompanyTimelineView.as_view()),
    path(r'kpi', KPIView.as_view()),
]
