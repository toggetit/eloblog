from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<entry_id>[0-9]+)/$', views.post, name='post'),
    #Предыдущие записи
    url(r'^page(?P<page>[0-9]+)/$', views.prevposts, name='prevposts'),
    url(r'^about/$', views.about, name='about'),
]
