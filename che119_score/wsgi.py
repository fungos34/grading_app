"""
WSGI config for che119_score project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'che119_score.settings')

application = get_wsgi_application()

# assuming your django settings file is at '/home/fungos/mysite/mysite/settings.py'
# and your manage.py is is at '/home/fungos/mysite/manage.py'
# path = '/home/fungos/fungos.pythonanywhere.com'