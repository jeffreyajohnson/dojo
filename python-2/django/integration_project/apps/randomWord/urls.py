from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^random_gen$', views.create_random_number, name='create'),
    url(r'^$', views.index, name='index'),
    
]
