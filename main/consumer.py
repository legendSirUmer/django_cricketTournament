import json
from channels.generic.websocket import AsyncWebsocketConsumer
from .models import LiveScore

class LiveScoreConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.match_id = self.scope['url_route']['kwargs']['match_id']
        self.group_name = f'live_score_{self.match_id}'

        # Join group
        await self.channel_layer.group_add(self.group_name, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        # Leave group
        await self.channel_layer.group_discard(self.group_name, self.channel_name)

    async def send_live_score(self, event):
        live_score = event['live_score']
        await self.send(text_data=json.dumps(live_score))