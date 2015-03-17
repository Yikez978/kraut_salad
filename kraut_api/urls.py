from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from kraut_api import views

urlpatterns = [
    url(r'^indicators/$', views.indicator_list),
    url(r'^indicators/(?P<pk>[0-9]+)/$', views.indicator_detail),
    url(r'^observables/$', views.observable_list),
    url(r'^observables/(?P<pk>[0-9]+)/$', views.observable_detail),
    url(r'^campaigns/$', views.campaign_list),
    url(r'^campaigns/(?P<pk>[0-9]+)/$', views.campaign_detail),
    url(r'^threatactors/$', views.threatactor_list),
    url(r'^threatactors/(?P<pk>[0-9]+)/$', views.threatactor_detail),
    url(r'^packages/$', views.package_list),
    url(r'^packages/(?P<pk>[0-9]+)/$', views.package_detail),
    url(r'^packagesd3/(?P<pk>[0-9]+)/$', views.package_d3),
]

urlpatterns = format_suffix_patterns(urlpatterns)
