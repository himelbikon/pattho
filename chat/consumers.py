import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from .models import Room, Message
from django.conf import settings

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_uuid = self.scope['url_route']['kwargs']['room_uuid']
        self.room_group_name = f'chat_{self.room_uuid}'

        # Check if user is authenticated and has permission to access room
        if self.scope.get('user', None).is_authenticated:
            user = self.scope['user']
            room = await self.get_room(self.room_uuid)

            if await self.is_user_in_room(self.room_uuid, user):
                # self.room_group_name = f'chat_{self.room_name}'
                await self.channel_layer.group_add(
                    self.room_group_name,
                    self.channel_name,
                )
                # print('User is in room'*100)
                await self.accept()
                # print('Connection accepted'*100)
            else:
                await self.close()
        else:
            await self.close()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name,
        )

        
    async def receive(self, text_data):
        # print(text_data, '-'*100)
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        # Save message to the database
        user = self.scope['user']
        await self.save_message(self.room_uuid, user, message)

        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'username': user.name,
                'user_image_url': settings.APP_URL + user.image_url,
            }
        )

    async def chat_message(self, event):
        # print(event, '-'*100)
        message = event['message']
        username = event['username']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message,
            'username': username,
            'user_image_url': event['user_image_url'],
        }))

    @database_sync_to_async
    def get_room(self, room_uuid):
        return Room.objects.get(uuid=room_uuid)

    @database_sync_to_async
    def save_message(self, room_uuid, user, message):
        room = Room.objects.get(uuid=room_uuid)
        Message.objects.create(room=room, sender=user, text=message)

    @database_sync_to_async
    def is_user_in_room(self, room_uuid, user):
        room = Room.objects.get(uuid=room_uuid)
        return user in room.users.all()