import os

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
import vibeus.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dating_app.settings')

application = get_asgi_application()

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": URLRouter(
        vibeus.routing.websocket_urlpatterns
    ),
})