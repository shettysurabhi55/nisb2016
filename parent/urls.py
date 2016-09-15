from django.conf.urls import url
from . import views

app_name = 'parent'

urlpatterns = [
        url(r'^$', views.index, name='index'),
        url(r'^events/$', views.events, name='events'),
	url(r'^about/$', views.about, name='about'),
	url(r'^cs/$', views.cs, name='cs'),
	url(r'^wie/$', views.wie, name='wie'),
	url(r'^members/$', views.members, name='members'), #to be worked on later
	url(r'^fg/$', views.fg, name='fg'), #focus groups : indicate "filling in soon" only
]
