from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^delete/(?P<id>(\d+))/(?P<verification>(\w+))$', views.delete, name='verify-delete'),
    url(r'^delete_course/(?P<id>\d+)$', views.delete_course, name='delete'),
    url(r'^add_course?$', views.add_course, name='add'),
    url(r'^$', views.index, name='index'),
    url(r'^enroll$', views.enroll, name='enroll'),
    url(r'^enroll_user$', views.enroll_user, name='enroll_user'),

]
