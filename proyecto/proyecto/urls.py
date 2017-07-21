from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [

    url(r'^universidades/', include('universidades.urls')),
    url(r'^admin/', include(admin.site.urls)),
]
