
#consumers.py

from channels.generic.websocket import AsyncWebsocketConsumer
import json
from asgiref.sync import async_to_sync


class Notification(AsyncWebsocketConsumer):
    
    async def connect(self):
        print("connect")
        self.room_name = "notifications_group"
        self.room_group_name = 'notifications_group'
        
        
        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name   
        )
        
        print("accept")
        
        await self.accept()
    
        print("connected")
        self.send(text_data=json.dumps({'status': 'connected'}))
        
        
    
    async def receive(self, text_data):
        print("receive")
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        
        print(message)
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
            }
        )
        
        
    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name,
        )
        

        
    async def send_notification(self, event):
        value = event.get('value')
        if value:
            print(event.get('value'))
            data = json.loads(value)
            data = json.loads(event.get('value'))
            print(data)
            await self.send(text_data=json.dumps({'payload': data}))
            print("send_totifications")
        else:
            print("Il messaggio è vuoto")
        
    async def chat_message(self, event):
        self.send(text_data=json.dumps(event))