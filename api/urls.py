from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import routers

from .views import *

router = routers.DefaultRouter()
router.register(r'countries', CountryView)
router.register(r'companies', CompanyView)

# urlpatterns = [
#     path('', include(router.urls)),
#     # path('countries/', CountryView.as_view()),
# ]

urlpatterns = router.urls

# urlpatterns = format_suffix_patterns(urlpatterns)
