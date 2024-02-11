from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
# Django imports
from future import standard_library
standard_library.install_aliases()
import django.dispatch 

# Piston imports
from .utils import send_consumer_mail

def consumer_post_save(sender, instance, created, **kwargs):
    send_consumer_mail(instance)

def consumer_post_delete(sender, instance, **kwargs):
    instance.status = 'canceled'
    send_consumer_mail(instance)


