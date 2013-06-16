

from datetime import datetime

from django.db import models
from django.core.exceptions import ObjectDoesNotExist

from pyurl.helpers.static_callable import Callable
from pyurl.settings import (MAX_PATH_LEN, MIN_HASH_LEN, MAX_HASH_LEN,
                            MAX_HASH_COLLISIONS_ALLOWED)
from pyurl import settings


#MAX_PATH_LEN = 2068

#MIN_HASH_LEN = 2
#MAX_HASH_LEN = 8

#MAX_HASH_COLLISIONS_ALLOWED = 10





PROTOCOLS = (
    (1, 'http'),
    (2, 'https'),
    (3, 'ftp'),
    (4, 'irc'),
    (5, 'aim'),
)

#class Protocol(models.Model):
#    name = models.CharField(max_length=5, choices=PROTOCOLS)
#
#    def __unicode__(self):
#        return self.name


class Url(models.Model):
    #protocol = models.ForeignKey(Protocol)
    path = models.CharField(max_length=MAX_PATH_LEN)
    hash = models.CharField(max_length=MAX_HASH_LEN)
    # DateTime of creation.
    #stamp_created = models.fields.DateTimeField(default=datetime.today)
    stamp_created = models.fields.DateTimeField(auto_now=True,
        auto_now_add=True)

    #def __init__(self, *args, **kw):

    def __unicode__(self):
        return self.path

    def __get_base_url(self):
        return '%s' % getattr(settings, 'SITE_BASE_URL')

    base_url = property(__get_base_url)

    def __get_short_url(self):
        return '%s/%s' % (getattr(settings, 'SITE_BASE_URL'), self.hash)

    short_url = property(__get_short_url)

    def __get_target_url(self):
        return '%s' % (self.path)

#    def __set_target_url(self, s):
        #from pyurl.helpers.tools import parse_url, unique_hash
        #prot, path = parse_url(url)
        #try:
            # Check to see if the url already exists.
            #u = Url.objects.get(protocol=Protocol.objects.get(name=prot), path=path)
        #except ObjectDoesNotExist:
            #hash = unique_hash(url)
            #u = Url(protocol=Protocol.objects.get(name=prot), path=path, hash=hash)

    target_url = property(__get_target_url)#, __set_target_url)

    def __get_short_url_len(self):
        return len(self.__get_short_url())

    short_url_len = property(__get_short_url_len)

    def __get_target_url_len(self):
        return len(self.__get_target_url())

    target_url_len = property(__get_target_url_len)
#    def factory(url):
        #from pyurl.helpers.tools import parse_url, unique_hash
        #prot, path = parse_url(url)
        #try:
            # Check to see if the url already exists.
            #u = Url.objects.get(protocol=Protocol.objects.get(name=prot), path=path)
        #except ObjectDoesNotExist:
            #hash = unique_hash(url)
            #u = Url(protocol=Protocol.objects.get(name=prot), path=path, hash=hash)
        #return u
#            # Make sure the exception is not on the hash column.
#            if (str(e).find('columns protocol_id, path are not unique') != -1 or
#                str(e).find('conflicts with persistent instance') != -1):
#            #if str(e).find('column hash is not unique') == -1
#                session.rollback()
#                return Url.query.filter_by(protocol=Protocol.get(prot),
#                    path=path).one()
#            raise e

#    factory = Callable(factory)



