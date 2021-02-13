"""
WSGI config for learning_log project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from dj_static import Cling # heroku

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'learning_log.settings')

# 能幫助正確提供靜態檔案的Cling，
# 並用來啟動應用程式 (本機也適用，所以不需要放在if區塊)
application = Cling(get_wsgi_application()) # heroku
