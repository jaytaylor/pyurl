
from django.contrib.auth import authenticate
from django.core.exceptions import ObjectDoesNotExist

from pyurl.rpc4django import rpcmethod

from pyurl.models import Url

# The doc string supports reST if docutils is installed.
@rpcmethod(name='pyurl.add', signature=['int', 'int', 'int'])
def add(a, b):
    '''Adds two numbers together
    >>> add(1, 2)
    3
    '''
    return a+b


@rpcmethod(name='pyurl.create',
    signature=['string', 'string', 'string', 'string', 'string'])
def xmlrpc_create(username, password, s_url, code=None):
    """
    Create a short url.  Optionally a specific code can be requested by the
    second parameter.
    """
    user = authenticate(username=username, password=password)
    if user is None:
        # Authentication failed.
        raise Exception('Invalid authentication credentials.')
    if not len(s_url):
        raise Exception('Url cannot be empty')
    try:
        new_url = Url.objects.get(path=s_url)
    except ObjectDoesNotExist:
        from pyurl.helpers.tools import unique_hash
        new_url = Url(path=s_url, hash=unique_hash(s_url, request=code))
        new_url.save()
    return new_url.short_url


@rpcmethod(name='pyurl.get', signature=['string', 'string'])
def xmlrpc_get(code):
    """
    Resolve the short url to the full one.  Can be the full shortened url or simply the code.
    e.g. -
    http://x/ASDF --> http://www.asdf.com
    ASDF --> http://www.asdf.com
    """
    if '/' in code:
        code = code[code.rindex('/'):code.rindex('/') + MAX_HASH_LEN]
    try:
        new_url = Url.objects.get(hash=code)
    except ObjectDoesNotExist:
        return ''
    return new_url.target_url


