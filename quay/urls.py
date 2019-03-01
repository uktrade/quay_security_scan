from quay.views import Home, VulnerabilitiesReport
from django.urls import path, include

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('push/', VulnerabilitiesReport.as_view(), name='report')
]
