

from django.shortcuts import render_to_response, get_object_or_404
from django.template import Context, loader, RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist

from pyurl.annoying.decorators import render_to

from pyurl import settings
from pyurl.settings import SITE_BASE_URL, VALIDATE_TARGET_LINKS, MAX_HASH_LEN
from pyurl.models import Url
from pyurl.helpers import validator
from pyurl.helpers.tools import parse_url
from pyurl.forms import UrlForm


def goog(request, *args):
    return HttpResponse('googleffffffffbd12c379')

@render_to('index.html')
def index(request, *args):
    #from django.contrib.auth import authenticate
    #if user is None:
    #    raise Exception('hmm')
    template_context = {
        'allow_custom': getattr(settings, 'ALLOW_CUSTOM_HASH', False),
        'url_form': UrlForm(request=request),
    }
    return template_context


@render_to('create.html')
def create(request):
    template_context = {
        'allow_custom': getattr(settings, 'ALLOW_CUSTOM_HASH', False),
    }
    if request.method == 'POST':
        #url = request.POST.get('url', '')
        #if url[0:len(SITE_BASE_URL)] == SITE_BASE_URL:
        #    raise PyurlViewException('Url cannot be to this website')
        #if getattr(settings, 'VALIDATE_TARGET_LINKS', False):
        #    result = validator.test_url(url)
        try:
            new_url = Url.objects.get(path=request.POST['path'])
            url_form = UrlForm(request=request)
        except ObjectDoesNotExist:
            url_form = UrlForm(data=request.POST, request=request)
            if url_form.is_valid():
                request, new_url = url_form.save()
        template_context['url'] = new_url
        template_context['url_form'] = url_form
    else:
        template_context['url_form'] = UrlForm(request=request)
    return template_context


#@render_to('create.html')
def forward(request, hash):
    try:
        url = Url.objects.get(hash=hash)
    except ObjectDoesNotExist:
        raise Http404
    #return {'url': url}
    return HttpResponseRedirect(url.path)


@render_to('preview.html')
def preview(request, hash):
    from pyurl.CutyCapt import cuty_capt
    template_context = {
        'allow_custom': getattr(settings, 'ALLOW_CUSTOM_HASH', False),
    }
    try:
        url = Url.objects.get(hash=hash)
    except ObjectDoesNotExist:
        raise Http404
    template_context['url'] = url
    preview_image_large = 'preview_cache/%s.png' % url.hash
    preview_image_small = 'preview_cache/%s_sm.png' % url.hash
    cuty_capt(url.target_url.encode('utf-8'),
        ('/var/www/jetlib.com/pyurl/%s' % preview_image_large).encode('utf-8'),
        ('/var/www/jetlib.com/pyurl/%s' % preview_image_small).encode('utf-8'))
    template_context['preview_image_small'] = preview_image_small
    template_context['preview_image_large'] = preview_image_large
    return template_context


#@rpcmethod(name='pyurl.create', signature=['string', 'string', 'string'])
#def xmlrpc_create(s_url, code=None):
#    """
#    Create a short url.  A code may be optionally be requested by the second
#    parameter.
#    """
#    try:
#        new_url = Url.objects.get(path=s_url)
#    except ObjectDoesNotExist:
#        from pyurl.helpers.tools import unique_hash
#        new_url = Url(path=s_url, hash=unique_hash(s_url, request=code))
#        new_url.save()
#    return new_url.short_url


#@rpcmethod(name='pyurl.get', signature=['string', 'string'])
#def xmlrpc_get(code):
#    """
#    Resolve the short url to the full one.  Can be the full shortened url or simply the code.
#    e.g. -
#    http://x/ASDF --> http://www.asdf.com
#    ASDF --> http://www.asdf.com
#    """
#    if '/' in code:
#        code = code[code.rindex('/'):code.rindex('/') + MAX_HASH_LEN]
#    try:
#        new_url = Url.objects.get(hash=code)
#    except ObjectDoesNotExist:
#        return ''
#    return new_url.target_url


#@render_to('result.html')
#def result(request):
#    template_context = {}
#    e = None
#    hash = None
#    if 'url' in request.POST.keys():
#        try:
#            u = Url.factory(request.POST['url'])
#            u.save()
#            hash = u.hash
#        except Exception, ex:
#            e = ex
#    else:
#        e = 'Missing required param: url'
#    return {'hash': hash, 'error_message': e}





