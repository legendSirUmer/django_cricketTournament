from django.urls import re_path
from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/live-score/(?P<match_id>\d+)/$', consumers.LiveScoreConsumer.as_asgi()),
]