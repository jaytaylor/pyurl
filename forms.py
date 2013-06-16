from django import forms
from django.core.exceptions import ObjectDoesNotExist
from django.conf import settings

from pyurl.models import Url
from pyurl.helpers.tools import unique_hash


class UrlForm(forms.ModelForm):

    def __init__(self, request, *args, **kw):
        super(UrlForm, self).__init__(*args, **kw)
        self.request = request

    def save(self, *args, **kw):
        try:
            # Check to see if the url already exists.
            u = Url.objects.get(path=self.instance.path)
        except ObjectDoesNotExist:
            self.instance.hash = unique_hash(self.instance.path,
                request=getattr(self.instance, 'hash', None))
            # Save url in the db.
            super(UrlForm, self).save(*args, **kw)

        # Add the url to the user session list.
        if self.request.session.get('url_list', False):
            if len(self.request.session['url_list']) >= getattr(settings,
                'MAX_URLS_PER_USER', 10):
                self.request.session['url_list'].pop(0)
            self.request.session['url_list'] += [self.instance.pk]
        else:
            self.request.session['url_list'] = [self.instance.pk]

        return self.request, self.instance

#    def clean(self):
#        pass #raise forms.ValidationError("You have forgotten about Fred!")


    class Meta:
        model = Url
        fields = (
            #'protocol',
            'path',
            'hash',
        )

#===============================================================================
# User Settings
#===============================================================================

#USERPREFS_0

