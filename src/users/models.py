from django.contrib.auth.models import AbstractUser, BaseUserManager, AbstractBaseUser, PermissionsMixin

from django.utils.translation import gettext as _

from django.db import models

import os
# Modelli di users

#Classe per la creazione dell'utente personalizzata
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model

from channels.layers import  get_channel_layer
from asgiref.sync import async_to_sync
import json


def get_upload_path(instance, filename):
    return os.path.join('images' , 'avatar' , str(instance.pk),filename)
    
class CustomUser(AbstractUser):
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(_('email address'), unique=True)
    nome = models.CharField(max_length=50)
    cognome = models.CharField(max_length=50)
    avatar = models.ImageField(upload_to=get_upload_path, blank=True, null=True,)
    is_active = models.BooleanField(default=True)
    is_verified = models.BooleanField(default=False)
    date_joined = models.DateTimeField(_('date joined'), auto_now_add=True)
    last_login = models.DateTimeField(_('last login'), auto_now=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']  

    def __str__(self):
        return self.username




class Notification(models.Model):
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    notification = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)


    def save(self, *args, **kwargs):
        print('Notification saving')
        channel_layer = get_channel_layer()
        notification_obj = Notification.objects.filter(is_read=False).count()
        data = {
            'count': notification_obj,
            'current_notification': self.notification,
            'account': f'{self.user.username}',
            
        }
            
        async_to_sync(channel_layer.group_send)(
            'test_consumer_group',
            {
                'type': 'send_notification',
                'value': json.dumps(data)
            }
        )
        print('Notification saved')
        super(Notification, self).save(*args, **kwargs)

