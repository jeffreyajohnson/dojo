from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^process_money$', views.process_money, name='process'),
    url(r'^', views.index, name='index'),

]