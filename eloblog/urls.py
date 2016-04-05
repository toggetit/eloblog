"""eloblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.contrib import admin

from django.conf.urls import include, url

from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^ckeditor/', include('ckeditor.urls')),

    url(r'^$', views.index),
    #Страницы постово
    url(r'^post/(?P<entry_id>[0-9]+)/$', views.post),
    #Предыдущие записи
    url(r'^page/(?P<pagenum>[0-9]+)/$', views.listing),
    
    url(r'^about/$', views.about),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
