"""fyp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import url
from django.urls import path
from django.contrib import admin
from account import views


from account.views import *

urlpatterns = [
    path('welcome/', views.welcome, name='welcome'),
    url(r'^admin/', admin.site.urls),
    # url(r'^index/$', home),
    path('crawl', views.crawl, name='crawl'),
    url(r'^login/$', login),
    url(r'^logout/$', logout),
    #url(r'', custreg),
    path('', views.custreg),
    path('info', views.info, name='info'),
]
