from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

import street3d.views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'gettingstarted.views.home', name='map'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', street3d.views.map, name='map'),
    url(r'^@\(([^,]+), ([^,]+)\),\(([^)]+),([^)]+)\):([^,]+),([^,]+),([^,]+),([^,]+),([^,]+),([^,]+)', street3d.views.mapWithLocation, name='map'),
    url(r'^render/@\(([^,]+), ([^,]+)\),\(([^)]+),([^)]+)\):([^,]+),([^,]+),([^,]+),([^,]+),([^,]+),([^,]+)', street3d.views.render_cross, name='render'),
    url(r'^db', street3d.views.db, name='db'),
    url(r'^admin/', include(admin.site.urls)),

)
