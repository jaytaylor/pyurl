import os, sys

PARENT_DIR = '/'.join(os.path.dirname(__file__).split('/')[0:-1])
sys.path.append(PARENT_DIR)

os.environ['DJANGO_SETTINGS_MODULE'] = 'pyurl.settings'

PROJECT_DIR = os.path.dirname(__file__)
os.environ['PYTHON_EGG_CACHE'] = '/'.join((PROJECT_DIR, '.python-eggs'))

import django.core.handlers.wsgi

application = django.core.handlers.wsgi.WSGIHandler()

import pyurl.monitor
pyurl.monitor.start(interval=1.0)

