from django.conf.urls import patterns, include, url
from django.contrib import admin
from login.views import *


urlpatterns = patterns('',
    url(r'^$', login), # If user is not login it will redirect to login page
    url(r'^register/$', register),
    url(r'^register/success/$', register_success),
    url(r'^home/$', home),
) 