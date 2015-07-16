from django.conf.urls import patterns, include, url
from django.contrib import admin
from login.views import *


urlpatterns = patterns('',
    url(r'^login/$', login_view), # If user is not login it will redirect to login page
    url(r'^logout/$', logout_view),
    url(r'^main/$', home),
) 