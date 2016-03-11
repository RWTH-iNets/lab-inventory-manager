from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^items/(?P<view_mode>[A-Za-z]+)/$', views.index, name='index'),
    # ex: /polls/5/vote/
    url(r'^search/$', views.search, name='search'),
    url(r'^category/(?P<category_id>[0-9]+)/$', views.category, name='category'),
    url(r'^details/(?P<item_id>[0-9]+)/$', views.details, name='details'),
]

