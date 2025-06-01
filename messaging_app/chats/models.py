from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    """
    Custom user model which doesn't have a username,
    but has a unique email and a date_of_birth.
    This model is used for both superusers and
    regular users as well.
    """
    # The inherited field 'username' is nullified, so it will
    # neither become a DB column nor will it be required.
    username = None
    email = models.EmailField(_("email address"), unique=True)
    date_of_birth = models.DateField(
        verbose_name="Birthday",
        null=True
    )

class Conversation(models.Model):
    """ create a conversation for each user """
    content = models.CharField(max_length=512)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Message(models.Model):
    """ create a message for each conversation which is related to each user"""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE)
    text = models.CharField(max_length=500)
