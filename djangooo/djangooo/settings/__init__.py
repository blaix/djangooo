import inspect
import os
from base import *

# modified version of:
# https://code.djangoproject.com/wiki/SplitSettings#modularmethod
module_name = os.getenv('DJANGO_ENV', 'local')
module = __import__(module_name, globals(), locals(), [])
for var_name, val in inspect.getmembers(module):
    if var_name.isupper():
        locals().update({var_name: val})
