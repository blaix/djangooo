"""
Following:
https://devcenter.heroku.com/articles/getting-started-with-django
"""

import os

from django.core.wsgi import get_wsgi_application
from dj_static import Cling

os.environ.setdefault('DJANGO_ENV', 'prod')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangooo.settings')
application = Cling(get_wsgi_application())
