from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
from builtins import filter
from future import standard_library
standard_library.install_aliases()
import hmac, base64

from django import forms
from django.conf import settings

class Form(forms.Form):
    pass

class ModelForm(forms.ModelForm):
    """
    Subclass of `forms.ModelForm` which makes sure
    that the initial values are present in the form
    data, so you don't have to send all old values
    for the form to actually validate. Django does not
    do this on its own, which is really annoying.
    """
    def merge_from_initial(self):
        self.data._mutable = True
        filt = lambda v: v not in list(self.data.keys())
        for field in filter(filt, getattr(self.Meta, 'fields', ())):
            self.data[field] = self.initial.get(field, None)


class OAuthAuthenticationForm(forms.Form):
    oauth_token = forms.CharField(widget=forms.HiddenInput)
    oauth_callback = forms.CharField(widget=forms.HiddenInput, required=False)
    authorize_access = forms.BooleanField(required=True)
