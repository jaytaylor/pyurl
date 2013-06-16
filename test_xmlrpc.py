

#from jsonrpc import ServiceProxy
#s = ServiceProxy('http://ghosted')
#print s.rpc4django.add(1,2,3)



from settings import *
from xmlrpclib import ServerProxy
s = ServerProxy(SITE_BASE_URL)#'http://ghosted')
print s.system.__doc__
print s.system.listMethods()
print s.pyurl.add(1,2)
for url,code in (('http://hotmail.com','hotmale'),
    ('https://gmail.com','gMaIL'),
    ('http://taylorproperties.com', 'toolonggggggggggg'),):
    print url,':',s.pyurl.create('admin','password',url, code)
#s.system.listMethods()
url = 'http://asfd.com'
print url,':',s.pyurl.create(url)
print '---'
print s.pyurl.get('hotmale')
print s.pyurl.get('hotwaleZ')

