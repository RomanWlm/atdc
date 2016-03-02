from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<product_name>[a-z]+)/search/$', views.search, name='search'),
]
