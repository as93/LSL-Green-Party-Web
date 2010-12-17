from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template, redirect_to

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^greenparty/', include('greenparty.foo.urls')),
    (r'^$',                                                 'greenparty.home.views.redirect'),
    (r'^(?P<language>(en|fr))/$',                           'greenparty.home.views.home'),
    (r'^(?P<language>(en|fr))/calendar/$',                  'greenparty.home.views.calendar'),
    (r'^(?P<language>(en|fr))/donate/$',                    'greenparty.home.views.donate'),
    (r'^(?P<language>(en|fr))/join/$',                      'greenparty.home.views.join'),


    (r'^(?P<language>(en|fr))/volunteer/',                  include('greenparty.volunteer.urls')),
    (r'^(?P<language>(en|fr))/media/',                      include('greenparty.news.urls')),

##    (r'^(?P<language>(en|fr))/bios/bio=(?P<bio_id>[\d]+)$', 'greenparty.news.views.bios'),
##
##    (r'^(?P<language>(en|fr))/about/$',                     'greenparty.home.views.about'),
##
##    (r'^(?P<language>(en|fr))/events/$',                    'greenparty.news.views.events'),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs'
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),


    #media path
    (r'^site_media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': './media/'}),
)
