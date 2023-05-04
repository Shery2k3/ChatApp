import json
from channels.generic.websocket import AsyncWebsocketConsumer


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']   # get room name from url
        self.room_group_name = 'chat_' + self.room_name     # create group name

        await self.channel_layer.group_add(    # add channel to group
            self.room_group_name,
            self.channel_name
        )   
        
        await self.channel_layer.group_send(    # send message to group
            self.room_group_name,
            {
                'type': 'tester_message',
                'tester': 'testing',
            }
        )
    
    async def tester_message(self, event):    # receive test message from group
        tester = event['tester']

        await self.send(text_data=json.dumps({
            'tester': tester,
        }))

    async def disconnect(self):    # remove channel from group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )
