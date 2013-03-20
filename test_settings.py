import os

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'local.db',
    }
}

INSTALLED_APPS = [
    'django_localflavor_gr'

]

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'wa3#e+bv-k$@o=-f6%e'
