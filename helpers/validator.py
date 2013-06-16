
from pyurl.helpers.wget import *
from pyurl.helpers.tools import parse_url


class UnrecognizedProtocolError(Exception):
    pass


def test_url(url):
    prot, path = parse_url(url)
    if prot == 'http':
        try:
            result = wget(url)
        except Exception, e:
            pass
    elif prot == 'https':
        return True
    elif prot == 'ftp':
        return True
    elif prot == 'irc':
        return True
    elif prot == 'aim':
        return True
    else:
        raise UnrecognizedProtocolError()
