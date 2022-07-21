from django.urls import path
from django.conf.urls import url
from .views import all_versions,all_devices,versions_date,highest_data,no_of_data,no_of_days,convert_version,exchange_tm_hm,delete_data_point

urlpatterns = [
    path('get-version',all_versions),
    path('get-dd',all_devices),
    path('get-version-on-date/',versions_date),
    url(r'^get-highest values ',highest_data),
    url(r'get-data-points ',no_of_data),
    url(r'^get-days-1-less-(?P<n>[0-9]+)-data',no_of_days),
    path('convert-version',convert_version),
    path('exchange-tm-hm',exchange_tm_hm),
    path('delete-data-point',delete_data_point),
]