#!/usr/bin/env python
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

import os
import sys

if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio.settings')  # Adjust the path
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),  # include our custom app urls here
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
