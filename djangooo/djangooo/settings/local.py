from os.path import realpath, join, dirname

src_root = realpath(join(dirname(__file__), '..', '..', '..'))

SECRET_KEY = 'q3w7%2z@*5=jx@*(7%i#sz2_$ediq=d3kge(eq&e2j0can5^c*'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': join(src_root, 'db.sqlite3'),
    }
}

TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'
NOSE_ARGS = ['--where=%s' % src_root, '--logging-filter=-django.db']
