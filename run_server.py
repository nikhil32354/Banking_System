#!/usr/bin/env python
import os
import sys
import django
from django.conf import settings
from django.core.management import execute_from_command_line

# Change to the correct directory
os.chdir(os.path.join(os.path.dirname(__file__), 'banking-system-master'))
sys.path.insert(0, os.getcwd())

# Set the Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'banking_system.settings')

if __name__ == '__main__':
    execute_from_command_line(['manage.py', 'runserver', '0.0.0.0:8000'])
