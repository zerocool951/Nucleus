from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'website.views.home', name='home'),
    url(r'^home', 'website.views.home', name='home'),
    url(r'^building1', 'website.views.building1', name='building1'),
    url(r'^building2', 'website.views.building2', name='building2'),
    url(r'^building3', 'website.views.building3', name='building3'),
    url(r'^finish', 'website.views.finish', name='finish'),
    url(r'^producten', 'website.views.producten', name='producten'),
    url(r'^order', 'website.views.order', name='order'),
    url(r'^contact', 'website.views.contact', name='contact'),
    

    #admin-page #[example] url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),

)
