from django.conf.urls import patterns, url

urlpatterns = patterns('universidades.views',
    url(r'^index', 'index', name="index"),
    url(r'^estadisticas', 'estadisticas', name="estadisticas"),
    url(r'^universidades', 'universidades', name="universidades"),
    url(r'^universidad', 'universidad', name="universidad"),
    url(r'^titulados', 'titulados', name="titulados"),
    url(r'^matriculados', 'matriculados', name="matriculados"),
    url(r'^mapa', 'mapa', name="mapa"),
    url(r'^graficos_u', 'graficos_u', name="graficos_u"),
    url(r'^docentes', 'docentes', name="docentes"),
    url(r'^$', 'index',name="index"),
)