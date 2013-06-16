import urllib2

class WgetError(Exception):
    pass

def wget(url, referer=''):
    opener = urllib2.build_opener()
    opener.addheaders = [
        ('User-agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.10) Gecko/2009042316 Firefox/3.0.10)'),
        ('Referer', referer),
    ]
    #print dir(opener)
    try:
        return opener.open(url).read()
    except urllib2.URLError, e:
        raise WgetError(str(e))

