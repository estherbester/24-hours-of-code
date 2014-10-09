from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'code24hours.teaser.views.placeholder', name='placeholder'),

    # disable admin urls for now, don't need it
    # url(r'^admin/', include(admin.site.urls)),
)
