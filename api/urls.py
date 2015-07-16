from django.conf.urls import patterns, include, url
from django.contrib import admin
from api.views import *



urlpatterns = patterns('',
    url(r'^addrecord/$', record), # If user is not login it will redirect to login page
    url(r'^search/', search),
) 