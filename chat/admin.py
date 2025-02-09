from django.contrib import admin
from . import models as chat_models

admin.site.register(chat_models.Room)
admin.site.register(chat_models.Message)
