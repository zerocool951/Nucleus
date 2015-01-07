from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'website.views.home', name='home'),
    url(r'^home', 'website.views.home', name='home'),
    url(r'^building', 'website.views.building', name='building'),
    url(r'^producten', 'website.views.producten', name='producten'),
    url(r'^about-us', 'website.views.aboutus', name='aboutus'),
    url(r'^contact', 'website.views.contact', name='contact'),
    

    #admin-page #[example] url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),

)
