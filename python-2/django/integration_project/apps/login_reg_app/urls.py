from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^users/new$', views.process, name='process'),
	url(r'^users/login$', views.login, name='login'),
	url(r'^delete_user/(?P<id>\d+)$', views.delete_user, name='delete_user'),
	url(r'^manage_user/$', views.manage_user, name='manage_user'),	
	
]
