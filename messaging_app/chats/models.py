from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
import uuid


class User(AbstractUser):
    """
    Custom user model which doesn't have a username,
    but has a unique email and a date_of_birth.
    This model is used for both superusers and
    regular users as well.
    """
    user_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    password = models.CharField(max_length=180)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=20)

class Conversation(models.Model):
    """ create a conversation for each user """
    conversation_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    participants = models.ManyToManyField(User)

class Message(models.Model):
    """ create a message for each conversation which is related to each user"""
    message_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, null = True, on_delete=models.CASCADE)
    conversation = models.ForeignKey(Conversation, null = True, on_delete=models.CASCADE)
    message_body = models.CharField(max_length=500)
    sent_at = models.DateField()
    created_at = models.DateField()
