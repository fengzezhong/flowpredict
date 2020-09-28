import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "flow_predict_interface.settings")

application = get_wsgi_application()
