from django.conf.urls import url
from kraut_sharing import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
]

