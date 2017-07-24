from django.conf.urls import patterns, url

urlpatterns = patterns('universidades.views',
    url(r'^index', 'index', name="index"),
    url(r'^estadisticas', 'estadisticas', name="estadisticas"),
    url(r'^universidades', 'universidades', name="universidades"),
    url(r'^universidad', 'universidad', name="universidad"),
    url(r'^$', 'index',name="index"),
)