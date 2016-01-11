from django.conf.urls import url
from django.contrib.auth import views

from . import views


urlpatterns = [
    #url(r'', views.articles),
    url(r'^index/', views.articles),
    url(r'^get/(?P<article_id>\d+)/', views.article),
    url(r'^language/(?P<language>[a-z\-]+)/', views.language),
    url(r'^create/', views.create),
    url(r'^like/(?P<article_id>\d+)/', views.like),
    url(r'^auth/', views.auth_view),
    url(r'^login/', views.login),
    url(r'^invalid/', views.invalid_login),
    url(r'^logout/', views.logout),
    url(r'^logged_in/', views.loggedin),
    url(r'^logout/', views.logout),

    url(r'^register/', views.register),
    url(r'^register_success/', views.register_success),
    
]