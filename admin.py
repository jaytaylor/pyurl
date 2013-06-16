
from django.contrib import admin

from pyurl.models import Url

#class ProtocolAdmin(admin.ModelAdmin):
#    pass

#admin.site.register(Protocol, ProtocolAdmin)


class UrlAdmin(admin.ModelAdmin):
    orderder=['-stamp_created']
    list_per_page = 25
    search_fields = ['path', 'hash']
    date_hierarchy = 'stamp_created'

admin.site.register(Url, UrlAdmin)


