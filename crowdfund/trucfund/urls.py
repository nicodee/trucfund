from django.conf.urls import patterns, url
from trucfund import views

urlpatterns = patterns('',	
	url(r'^$', views.index, name='index'),
	url(r'^discover/$', views.discover, name='discover'),
	url(r'^project/$', views.project, name='project'),
	url(r'^profile/$', views.profile, name='profile'),
	url(r'^create/$', views.create, name='create'),
)