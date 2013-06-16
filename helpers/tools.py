
import hashlib
import base64
import re

from django.core.exceptions import ObjectDoesNotExist

from pyurl.settings import (MAX_PATH_LEN, MIN_HASH_LEN, MAX_HASH_LEN,
                            MAX_HASH_COLLISIONS_ALLOWED,
                            TRUNC_LONG_HASH_REQUESTS, VALID_HASH_CHARS)
from pyurl import settings
from pyurl.models import Url

class HashCollisionThresholdReachedException(Exception):
    """
    Raised by unique_hash() when the number of collisions exceeds the limit.
    """
    pass


request_re = re.compile('''^[%s]{%s,%s}$''' % (
        getattr(settings, 'VALID_HASH_CHARS'),
        getattr(settings, 'MIN_HASH_LEN'),
        getattr(settings, 'MAX_HASH_LEN'),
    )
)

def unique_hash(s, hlen=MIN_HASH_LEN, attempt=1, **kw):
    """
    @param **kw: 'request' may be passed to request a specific hash code.
        Request will only be allowed if enabled in the configuration settings.
    """
    if attempt > MAX_HASH_COLLISIONS_ALLOWED:
        raise HashCollisionThresholdReachedException()
    if attempt == 1 and getattr(settings, 'ALLOW_CUSTOM_HASH', False) and \
        kw.get('request', None) != None and request_re.match(kw['request']):
        if len(kw['request']) <= MAX_HASH_LEN:
            # Hash request length is valid, so attempt to use it.
            hash = kw['request']
        elif TRUNC_LONG_HASH_REQUESTS:
            # Determine what action to take.  The long hash request will either
            # be truncated or ignored, depending on the configuration setting.
            hash = kw['request'][0:MAX_HASH_LEN]
        else:
            hash = hashlib.md5(s).hexdigest()[0:hlen]
    else:
        #hash = hashlib.sha224(base64.urlsafe_b64encode(s)).hexdigest()[0:hlen]
        hash = hashlib.md5(s).hexdigest()[0:hlen]
    try:
        Url.objects.get(hash=hash)
    except ObjectDoesNotExist:
        return u'%s' % hash
    #print 'COLLISION FOUND ON HASH: %s' % hash
    if hlen < MAX_HASH_LEN:
        return unique_hash(s, hlen + 1)
    else:
        s += '%s' % datetime.today().microsecond
        return unique_hash(s, attempt + 1)


def parse_url(url):
    protocol = url[0:url.find('://')]
    path = url[url.find('://') + 3:]
    return (protocol, path)

