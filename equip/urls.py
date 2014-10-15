from django.conf.urls import patterns, include, url
from equipment import views

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^equipment/', include('equipment.urls')),
                        url(r'^$', views.index, name='index'),
#                       url(r'^departments/', include('equipment.urls')),
#                       url(r'^users/', include('equipment.urls')),
                       url(r'^admin/', include(admin.site.urls)),
    
)
