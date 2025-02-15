from django.db import models
from core.utils import generate_random_code

class Room(models.Model):
    UUID_LENGTH = 20

    name = models.CharField(max_length=255)
    logo = models.ImageField(upload_to='chat/room/logo/', null=True, blank=True)
    users = models.ManyToManyField('user.User', blank=True)

    uuid = models.CharField(max_length=255, unique=True)
    created_at = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return f'{self.name} - {self.uuid}'

    def save(self, *args, **kwargs):
        if not self.id:
            self.uuid = generate_random_code(self.UUID_LENGTH)
        super().save(*args, **kwargs)

    @property
    def is_group(self):
        return self.users.count() > 2

    @property
    def last_message(self):
        return self.messages.first()


class Message(models.Model):
    UUID_LENGTH = 30

    sender = models.ForeignKey('user.User', on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name="messages")
    text = models.TextField()

    reply = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    seener = models.ManyToManyField('user.User', blank=True, related_name='seeners')

    uuid = models.CharField(max_length=UUID_LENGTH, unique=True)
    created_at = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return f'{self.room.name} - {self.text}'

    def save(self, *args, **kwargs):
        if not self.id:
            self.uuid = generate_random_code(self.UUID_LENGTH)
        super().save(*args, **kwargs)
