"""
WSGI config for CarService project on InfinityFree.

This file is used by Passenger (InfinityFree's WSGI application server).
"""

import sys
import os

# Add the project directory to the path
sys.path.insert(0, os.path.dirname(__file__))

# Set the Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'CarService.settings')

# Import Django WSGI application
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
