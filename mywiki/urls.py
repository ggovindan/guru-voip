from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mywiki.views.home', name='home'),
    # url(r'^mywiki/', include('mywiki.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
      url(r'^mywiki/(?P<page_name>[^/]+)/edit$', 'wiki.views.editpage'),
      url(r'^mywiki/(?P<page_name>[^/]+)/save$', 'wiki.views.savepage'),
      url(r'^mywiki/(?P<page_name>[^/]+)/$', 'wiki.views.viewpage'),
      url(r'^adminpage/$', 'wiki.views.adminpage'),
      url(r'^(?P<userid>[^/]+)/$', 'wiki.views.mainpage'),
)
