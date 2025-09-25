from django.urls import re_path, path
from . import consumers

websocket_urlpatters = [
    #ath("ws/chat/<str:room_name>/", consumers.ChatConsumer.as_asgi()),#metodo simple menos estricto
    re_path(r"ws/chat/(?P<room_name>\w+)/$", consumers.ChatConsumer.as_asgi()), #raw metodo mas estricto
]