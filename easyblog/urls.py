from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^journal/$', 'easyblog.journal.views.index'),
    url(r'^journal/(?P<slug>[\w\-\_\+]+)/$',
        'easyblog.journal.views.show', name='entry'),
    url(r'^category/(?P<category_slug>[\w\-\_\+]+)/$',
        'easyblog.journal.views.index', name='category'),
    url(r'^gallery/(?P<slug>[\w\-\_\+]+)/$',
        'easyblog.image.views.gallery', name='gallery')
)

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT
        })
    )

