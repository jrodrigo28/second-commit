"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
import django.contrib.auth.views
from . import views

urlpatterns = [
    url(r'^$', views.article_list,name ='article_list'),
    url(r'^article/(?P<pk>\d+)/$',views.article_detail,name='article_detail'),
    url(r'^new/article/$',views.new_article,name='new_article'),
    url(r'^edit/(?P<pk>\d+)/article/$',views.edit_article,name='edit_article'),
    url(r'^delete/(?P<pk>\d+)/article/$',views.delete_article,name='delete_article'),
    url(r'^accounts/login/$',django.contrib.auth.views.login,name='login'),
    url(r'^accounts/logout/$',django.contrib.auth.views.logout,name='logout',kwargs={'next_page':'/'}),
    url(r'^articlelist/(?P<team>[\w\-]+)/$',views.team_article_list,name='team_article_list'),
    
]
