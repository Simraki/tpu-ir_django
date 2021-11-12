from rest_framework import routers

from .views import *

router = routers.DefaultRouter()
router.register(r'countries', CountryView)
router.register(r'companies', CompanyView)
router.register(r'agreements', AgreementView)
router.register(r'representatives', RepresentativeView)
router.register(r'agreement_types', AgreementTypeView)
router.register(r'kpi', KPIView, basename='kpi')

urlpatterns = router.urls
