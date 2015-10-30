from app.settings import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join( PROJECT_DIR , 'sqlite3.db'),
    }
}
#INSTALLED_APPS += ('debug_toolbar',)


