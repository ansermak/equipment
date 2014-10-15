from django.conf.urls import patterns, url

from equipment import views

urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
                        url(r'^computers/$', views.computers, name='computers'),
                        url(r'^computers/(?P<computer_inum>\d+)/$', views.computer, name='computer'),
                        url(r'^departments/$', views.departments, name='departments'),
                        url(r'^departments/(?P<department>[a-zA-Z ]+)/$', views.department, name='department'),
                        url(r'^users/(?P<user>[a-zA-Z ]+)/$', views.user, name='user'),
                        url(r'^monitors/(?P<monitor_inum>\d+)/$', views.monitor, name='monitor'),
                        url(r'^upses/(?P<ups_inum>\d+)/$', views.ups, name='ups'),
                        #url(r'^upses/(?P<ups_inum>\d+)/$', views.ups, name='ups'),
)