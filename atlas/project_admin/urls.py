from django.conf.urls import url
from django.contrib.auth import views as auth_views

from . import views

app_name = 'project_admin'
urlpatterns = [
	url(r'^$', views.DashboardView, name='index'),
    url(r'^login/$', auth_views.login, {'template_name': 'project_admin/login.html'}),
	url(r'^projects/(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
	url(r'^json/(?P<mode>[a-z]+)/$', views.json, name='json'),
	url(r'^projects/add/$', views.get_project, name='get_project'),
	url(r'^projects/(?P<mode>[a-z]+)/$', views.projectsView, name='projects'),
	url(r'^clients/add/$', views.get_client, name='get_client'),
	url(r'^items/add/$', views.get_itemcost, name='get_itemcost'),
]