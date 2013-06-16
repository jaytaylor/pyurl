from django.conf.urls.defaults import *

from pyurl.settings import MIN_HASH_LEN, MAX_HASH_LEN, VALID_HASH_CHARS
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^willowvillagesquare/', include('willowvillagesquare.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    #(r'^(XML)?RPC2\/?$', 'pyurl.rpc4django.views.serve_rpc_request'),
    url(r'^googlehostedservice.html$', 'pyurl.views.goog', name='googlehostedservice'),
    url(r'^RPC2$', 'pyurl.rpc4django.views.serve_rpc_request', name='rpc'),
    url(r'^(index\/?)?$', 'pyurl.views.index', name='site-homepage'),
    url(r'^create\/?$', 'pyurl.views.create', name='create'),
    url(r'^preview\/([%s]{%s,%s})\/?$' % (VALID_HASH_CHARS, MIN_HASH_LEN,
        MAX_HASH_LEN), 'pyurl.views.preview', name='preview'),
    (r'^admin\/', include(admin.site.urls)),
    url(r'^([%s]{%s,%s})$' % (VALID_HASH_CHARS, MIN_HASH_LEN, MAX_HASH_LEN),
        'pyurl.views.forward', name='forward'),
    #(r'^admin/', include(admin.site.urls)),
    #(r'^media/(.*)$', 'django.views.main.serve', {'document_root': './admin_media'}),
#    (r'^site_media/(.*)$', 'django.views.static.serve', {'document_root': '/path/to/folder/media'}),
)

