from settings_default import *

DEBUG = True
DEBUG = False
TRANSLIM = 6000

DATABASES = {
  'default': {
    'ENGINE': 'django.db.backends.mysql',
    'NAME': 'valdx',
    'USER': 'vald',
    'PASSWORD': 'V@ld',
#    'OPTIONS': {
#           "init_command": "SET storage_engine=INNODB",
#    }   
  },
  'valdx': {
    'ENGINE': 'django.db.backends.mysql',
    'NAME': 'valdx',
    'USER': 'vald',
    'PASSWORD': 'V@ld',
  },
  'test': {
    'ENGINE': 'django.db.backends.mysql',
    'NAME': 'test',
    'USER': 'vald',
    'PASSWORD': 'V@ld',
  },
  'memory': {
    'ENGINE': 'django.db.backends.mysql',
    'NAME': 'vald',
    'USER': 'vald',
    'PASSWORD': 'V@ld',
    'OPTIONS': {
           "init_command": "SET storage_engine=MEMORY",
    }
  },
  'sqlite': {
    'ENGINE': 'django.db.backends.sqlite3',
    'NAME': 'vald.db',
  }

}

ADMINS = (('Thomas', 'thomas@marquart.se'),)
#LOGGING['handlers']['logfile']['filename'] = '/tmp/mylog.log'
EXAMPLE_QUERIES = ['SELECT ALL WHERE RadTransWavelength > 4000 AND RadTransWavelength < 4005',
                   'SELECT ALL WHERE AtomSymbol = U']
SERVER_EMAIL = 'vamdc@vald.astro.uu.se'

