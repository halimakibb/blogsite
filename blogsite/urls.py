"""blogsite URL Configuration

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
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url, include
from django.contrib import admin
from blog import urls
from . import views

urlpatterns = [
    url(r'^blog/', include('blog.urls')),
    url(r'^admin/', admin.site.urls),
    
    #user auth
    
    url(r'^accounts/login/', views.login),
    url(r'^accounts/auth/', views.auth_view),
    url(r'^accounts/logout/', views.logout),
    url(r'^accounts/loggedin/', views.loggedin),
    url(r'^accounts/invalid/', views.invalid_login),
    url(r'^accounts/register/', views.register_user),
    url(r'^accounts/register_success/', views.register_success),
    
    #tiny mce
    
    url(r'^tinymce/', include('tinymce.urls')),
]
